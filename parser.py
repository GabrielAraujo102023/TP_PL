import ply.yacc
from lex import tokens, literals
import sys
import vm_code_generator as code_generator
import Node

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

# Guarda o nome das funções e o seu código VM
functions = {}

def vm_functions():
    global functions
    res = '\n'
    for name, code in functions.items():
        res += name + ':\n'
        res += code + '\n'
    return res

init_vars = 0

def p_Expressions(p):
    """
    Expressions : Expressions Expression
                | Expression
    """
    if len(p) == 2:
        p[0] = Node.Expressions(t="single", expression=p[1])
    else:
        p[0] = Node.Expressions(t="mult", expressions=p[1] ,expression=p[2])

def p_expression_arith(p):
    """
    Expression : Expression Expression ArithmeticOp
    """
    p[0] = Node.Expression('exp', p[1], p[2], p[3])

def p_expression_num(p):
    """
    Expression : NUM
    """
    p[0] = Node.Number(p[1])

def p_arithmeticop(p):
    """
    ArithmeticOp : '+'
                 | '-'
                 | '*'
                 | '/'
                 | MOD
                 | NEGATE
    """
    p[0] = Node.ArithmeticOperation(p[1])

def p_print_expression(p):
    """
    Expression : Expression '.'
    """
    p[0] = Node.Expression('print', p[1])

def p_create_function(p):
    """
    Expression : ':' ID '(' Arguments '-' '-' ID ')' Expressions ';'
    """
    p[0] = Node.Node()
    if p[2] in functions.keys():
        print(f"Erro: Duas funções declaradas com o mesmo nome: {p[2]}", file=sys.stderr)
        sys.exit(0)
    else:
        global init_vars
        init_vars += 1
        functions[p[2]] = p[9].vm_code()

def p_Arguments(p):
    """
    Arguments : Arguments ID
              | ID
    """
    if len(p) == 2:
        p[0] = '1'
    else:
        p[0] = str(int(p[1]) + 1)


def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False


# Parsing
parser = ply.yacc.yacc()

with open(sys.argv[1], 'r') as forth_file:
    ast = parser.parse(forth_file.read())

vm_code = ''

for i in range(init_vars):
    vm_code += 'PUSHI 0\n'

vm_code += 'START\n'

vm_code += ast.vm_code()

vm_code += 'STOP'

vm_code += vm_functions()

print(vm_code)