import ply.lex as lex
import sys
import re

literals = ['+', '-', '*', '/', '.', '@', '!', '?', ';', ':', '(', ')']

tokens = (
    'NUM',
    'VARIABLE',
    'ID',
    'MOD',
    'NEGATE',
    'ARGS'
)

t_NUM = r'\d+'
t_VARIABLE = r'[vV][aA][rR][iI][aA][bB][lL][eE]'
t_ID = r'[a-zA-Z]\S*'
t_MOD = r'[mM][oO][dD]'
t_NEGATE = r'[nN][eE][gG][aA][tT][eE]'

t_ignore = ' \n\t'

def t_error(t):
    print('Carácter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

text = ''
with open(sys.argv[1], 'r') as code:
    for line in code:
        text += line

def t_ARGS(t):
    r'( [a-z] )+ -- [a-z]'
    m = re.match(r'\(( [a-z] )+ -- [a-z]\)', t.value)
    t.value = len(m.group(1).split(' '))

lexer.input(text)

if __name__ == '__main__':
    while tok := lexer.token():
        print(tok)