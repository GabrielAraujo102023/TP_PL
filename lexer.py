from ply import lex
import sys

tokens = [
    'FLOAT',
    'INT',
    'ARITHMETIC_OP',
    'DOT',
    'CHAR',
    'OVER',
    'EMIT',
    'AGAIN',
    'VARIABLE',
    'BEGIN',
    'UNTIL',
    'WHILE',
    'REPEAT',
    'DROP',
    'DUP',
    'KEY',
    'SWAP',
    'CR',
    'IF',
    'DO',
    'LOOP',
    'PLUS_LOOP',
    'THEN',
    'ROT',
    'CONSTANT',
    'ELSE',
    'DOT_QUOTE',
    'WORD',
    'DOUBLE_HIFEN',
    'COMPARISON',
    'INC_VAR',
    'SPACE'
]
t_DOT = r'\.'
literals = [':', ';', '(', ')', '!', '@', '?']


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_DOUBLE_HIFEN(t):
    r'--'
    return t


def t_COMPARISON(t):
    r'<>|0=|0<|0>|>|<|=|(?i)and|(?i)or'
    return t


def t_PLUS_LOOP(t):
    r'(?i)\+loop'
    return t


def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INC_VAR(t):
    r'\+!'
    return t


def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_VARIABLE(t):
    r'(?i)variable[ \t]+([a-z_]+)'
    t.value = t.value.split()[1]
    return t


def t_CONSTANT(t):
    r'(?i)constant[ \t]+([a-z_]+)'
    t.value = t.value.split()[1]
    return t


def t_ARITHMETIC_OP(t):
    r'[\+\-\*/]|(?i)mod|(?i)negate'
    t.value = t.value.lower()
    return t


def t_DOT_QUOTE(t):
    r'\." ([^"]*)"'
    t.value = t.value[3:-1]
    return t


def t_BEGIN(t):
    r'(?i)begin'
    return t


def t_KEY(t):
    r'(?i)key'
    return t


def t_SPACE(t):
    r'(?i)space'
    return t


def t_REPEAT(t):
    r'(?i)repeat'
    return t


def t_WHILE(t):
    r'(?i)while'
    return t


def t_AGAIN(t):
    r'(?i)again'
    return t


def t_UNTIL(t):
    r'(?i)until'
    return t


def t_DO(t):
    r'(?i)do'
    return t


def t_LOOP(t):
    r'(?i)loop'
    return t


def t_CR(t):
    r'(?i)cr'
    return t


def t_DROP(t):
    r'(?i)drop|(?i)2drop'
    if '2' in t.value:
        t.value = 2
    else:
        t.value = 1
    return t


def t_IF(t):
    r'(?i)if'
    return t


def t_THEN(t):
    r'(?i)then'
    return t


def t_ELSE(t):
    r'(?i)else'
    return t


def t_SWAP(t):
    r'(?i)swap'
    return t


def t_ROT(t):
    r'(?i)rot'
    return t


def t_CHAR(t):
    r'(?i)char[ \t]+(.)'
    t.value = t.value.split()[1]
    return t


def t_DUP(t):
    r'(?i)dup|(?i)2dup'
    if '2' in t.value:
        t.value = 2
    else:
        t.value = 1
    return t


def t_OVER(t):
    r'(?i)over|(?i)2over'
    if '2' in t.value:
        t.value = 2
    else:
        t.value = 1
    return t


def t_EMIT(t):
    r'(i?)emit'
    return t


def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
text = ''
with open(sys.argv[1], 'r') as code:
    for line in code:
        text += line

lexer.input(text)

if __name__ == '__main__':
    while tok := lexer.token():
        print(tok)
        print(tok.value)
