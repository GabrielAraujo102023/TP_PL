from ply import yacc
from lexerv2 import tokens, literals
import sys
import nodev2

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

functions = {}
init_vars = 0


def p_program(p):
    """program : statements"""
    p[0] = nodev2.Program(p[1])


def p_statements(p):
    """statements : statement
                  | statement statements"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_statement(p):
    """statement : function
                 | expression
                 | default_function"""
    p[0] = p[1]


def p_function(p):
    """function : ':' WORD '(' arguments DOUBLE_HIFEN WORD ')' function_body ';'
                | ':' WORD function_body ';'"""
    global functions
    p[0] = nodev2.Node()
    if p[2] in functions.keys():
        print(f"Error: Two functions declared with the same name: {p[2]}", file=sys.stderr)
        sys.exit(0)
    else:
        global init_vars
        init_vars += len(p[4])
        if len(p) > 5:
            p[0] = nodev2.Function(p[2], p[8], len(p[4]))
        else:
            p[0] = nodev2.Function(p[2], p[3])
        functions[p[2]] = p[0]


def p_function_body(p):
    """function_body : statements"""
    p[0] = nodev2.FunctionBody(p[1])


def p_arguments(p):
    """
    arguments : arguments WORD
              | WORD
    """
    if len(p) == 2:
        p[0] = [p[1]]  # If there's only one argument, store it in a list
    else:
        p[0] = p[1] + [p[2]]


def p_expression(p):
    """expression : literal
                  | operation"""
    p[0] = p[1]


def p_literal(p):
    """literal : NUMBER
               | WORD"""
    global functions
    if p[1] in functions:
        p[0] = nodev2.Literal(p[1], functions[p[1]])
    else:
        p[0] = nodev2.Literal(p[1], functions)


def p_operation(p):
    """operation : ARITHMETIC_OP"""
    p[0] = nodev2.Operation(p[1])


def p_default_function(p):
    """default_function : DOT
                        | DOT_QUOTE
                        | CHAR
                        | EMIT"""
    p[0] = nodev2.DefaultFunction(p.slice[1].type, p.slice[1].value)


def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False


# Parsing
parser = yacc.yacc()

with open(sys.argv[1], 'r') as forth_file:
    ast = parser.parse(forth_file.read())
    print(ast)

program_code = ast.vm_code()
functions_code = ""
push_var = ""

for func in functions.values():
    push_var += "pushi 0\n"
    functions_code += func.vm_code()

for var in range(init_vars):
    push_var += "pushi 0\n"

vm_code = push_var + program_code + functions_code
print(vm_code)  # Print the generated VM code from the AST
