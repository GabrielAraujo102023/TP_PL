import ply.yacc
from lex import tokens, literals
import sys
import vm_code_generator as code_generator
import Node

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

vm_code = 'START\n'

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
                 | NEGATE
    """
    p[0] = Node.ArithmeticOperation(p[1])

def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False

parser = ply.yacc.yacc()

with open(sys.argv[1], 'r') as code:
    asd = parser.parse(code.read())

vm_code += asd.vm_code()

vm_code += 'STOP'

print(vm_code)