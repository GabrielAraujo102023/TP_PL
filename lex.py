import ply.lex as lex
import sys

literals = ['+', '-', '*', '/', '.', '@', '!', '?', ';', ':']

tokens = (
    'NUM',
    'VARIABLE',
    'ID',
    'MOD',
    'NEGATE',
    'ABS',
    'MIN',
    'MAX'
)

t_NUM = r'\d+'
t_VARIABLE = r'[vV][aA][rR][iI][aA][bB][lL][eE]'
t_ID = r'[a-zA-Z]\S*'
t_MOD = r'[mM][oO][dD]'
t_ABS = r'[aA][bB][sS]'
t_MIN = r'[mM][iI][nN]'
t_MAX = r'[mM][aA][xX]'

t_ignore = ' \n\t'

def t_error(t):
    print('Carácter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

text = ''
with open(sys.argv[1], 'r') as code:
    for line in code:
        text += line

lexer.input(text)