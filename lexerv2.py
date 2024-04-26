from ply import lex
import sys

tokens = [
    'NUMBER',
    'ARITHMETIC_OP',
    'DOT',
    'CHAR',
    'EMIT',
    'DUP',
    'DOT_QUOTE',
    'WORD',
    'DOUBLE_HIFEN'
]
t_DOT = r'\.'
literals = [':', ';', '(', ')']


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_DOUBLE_HIFEN(t):
    r'--'
    return t

def t_ARITHMETIC_OP(t):
    r'[\+\-\*/]|(?i)mod|(?i)negate'
    t.value = t.value.lower()
    return t


def t_DOT_QUOTE(t):
    r'\." ([^"]*)"'
    t.value = t.value[3:-1]
    return t


def t_CHAR(t):
    r'(?i)char[ \t]+(.)'
    t.value = t.value.split()[1]
    return t


def t_DUP(t):
    r'(?i)dup'
    return t


def t_EMIT(t):
    r'(i?)emit'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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
