import ply.yacc
from lex import tokens, literals
import sys
import vm_code_generator as code_generator
import Node

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

vm_code = 'START\n'

def p_S(p):
    """
    S : Expression '$'
    """
    p[0] = Node.S(p[1])

def p_expression(p):
    """
    Expression : Expression ArithmeticOp
               | Expression Literal
               | '$'
    """
    p[0] = Node.Expression('doesnt matter', p[1], p[2])

def p_arithmeticop(p):
    """
    ArithmeticOp : '+'
                 | '-'
                 | '*'
                 | '/'
                 | NEGATE
    """
    p[0] = Node.ArithmeticOperation(p[1])

#Adicionar strings aqui
def p_literal(p):
    """
    Literal : NUM
    """
    p[0] = Node.Literal(p[1])

def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False

parser = ply.yacc.yacc()

with open(sys.argv[1], 'r') as code:
    asd = parser.parse(code.read())

print(asd)

vm_code += 'STOP'

#print(vm_code)