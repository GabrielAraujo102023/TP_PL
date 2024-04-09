import ply.yacc
from lex import tokens, literals
import sys
import vm_code_generator as code_generator

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

vm_code = 'START\n'

def p_expression(p):
    """
    Expression : ArithmeticOp
               | Literal
    """

def p_arithmeticop(p):
    """
    ArithmeticOp : '+'
                 | '-'
                 | '*'
                 | '/'
                 | MOD
                 | NEGATE
                 | ABS
                 | MIN
                 | MAX
    """
    global vm_code
    vm_code += code_generator.arithmetic_operations(p[1])

#Adicionar strings aqui
def p_literal(p):
    """
    Literal : NUM
    """
    global vm_code

def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False

parser = ply.yacc.yacc()

with open(sys.argv[1], 'r') as code:
    for line in code:
        parser.parse(line)

vm_code += 'STOP'

print(vm_code)