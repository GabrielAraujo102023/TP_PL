import re
def arithmetic_operations(symbol):
    if symbol == '+':
        return 'ADD\n'
    elif symbol == '-':
        return 'SUB\n'
    elif symbol == '*':
        return 'MUL\n'
    elif symbol == '/':
        return 'DIV\n'
    elif symbol == 'mod':
        return 'MOD\n'

def literals(literal):
    if re.match(r'\d+', literal):
        return f'PUSHI {literal}\n'
    """
    elif literal == 'false' or literal == 'true':
        # tratar boolean
    else:
        # tratar string
    """