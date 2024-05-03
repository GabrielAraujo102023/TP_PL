from ply import yacc
from lexerv2 import tokens, literals
import sys
import nodev2

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

functions = {}
init_vars = 0
previous_num = None
frame_pointer = 0
stack_pointer = 0
total_ifs = 0


def p_program(p):
    """program : statements"""
    p[0] = nodev2.Program(p[1])


def p_statements(p):
    """
    statements : statement
               | statement statements
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_statement(p):
    """
    statement : function
              | condition_construct
              | operation
              | comparison
              | forth_function
              | words
              | num
    """
    p[0] = p[1]
    

def p_condition_construct(p):
    """
    condition_construct : comparison IF statements THEN
                        | comparison IF statements ELSE statements THEN
    """
    global total_ifs
    total_ifs += 1
    # p[0] = nodev2.Node()
    if len(p) == 8:
        p[0] = nodev2.ConditionConstruct(p[1], p[3], total_ifs)
    else:
        p[0] = nodev2.ConditionConstruct(p[1], p[3], total_ifs, p[5])


def p_function(p):
    """
    function : ':' WORD '(' arguments DOUBLE_HIFEN WORD ')' function_body ';'
             | ':' WORD function_body ';'
    """
    global functions
    
    if p[2] in functions.keys():
        print(f"Error: Two functions declared with the same name: {p[2]}", file=sys.stderr)
        sys.exit(0)
    else:
        p[0] = nodev2.Node()
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
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_operation(p):
    """operation : ARITHMETIC_OP"""
    p[0] = nodev2.Operation(p[1], previous_num)


def p_comparison(p):
    """comparison : COMPARISON"""
    p[0] = nodev2.Comparison(p[1], previous_num)


def p_num(p):
    """
    num : INT
        | FLOAT
    """
    p[0] = nodev2.Num(p[1])
    global previous_num
    previous_num = p[0].type


def p_words(p):
    """
    words : WORD
    """
    global functions
    if p[1] in functions:
        p[0] = nodev2.Word(p[1], functions[p[1]])
    else:
        p[0] = nodev2.Word(p[1])


def p_forth_function(p):
    """
    forth_function : DOT
                   | DOT_QUOTE
                   | CHAR
                   | EMIT
                   | DUP
                   | SWAP
                   | CR
                   | KEY
                   | DROP
    """
    p[0] = nodev2.ForthFunction(p.slice[1].type, p.slice[1].value)


def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False


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
    stack_pointer += 1

if push_var:
    push_var += '\n'

vm_code = push_var + program_code + functions_code
print(vm_code)
