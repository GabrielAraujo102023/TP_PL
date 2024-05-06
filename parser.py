from ply import yacc
from lexer import tokens, literals
import sys
import node

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

previous_num = None
functions = {}
variables = {}


def p_program(p):
    """program : statements"""
    p[0] = node.Program(p[1])


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
              | loop
              | conditional
              | operation
              | comparison
              | forth_function
              | words
              | num
              | variable
    """
    p[0] = p[1]
    

def p_variable(p):
    """variable : VARIABLE
                | CONSTANT"""
    global variables
    name = p.slice[1].value
    if name in variables:
        print(f"Error: Two variables declared with the same name: {p[2]}", file=sys.stderr)
        sys.exit(0)

    if p.slice[1].type == 'VARIABLE':
        p[0] = node.Variable(name)
    else:
        p[0] = node.Constant(name)

    variables[name] = [p[0]]


def p_loop(p):
    """loop : DO statements LOOP
            | DO statements PLUS_LOOP
            | BEGIN statements UNTIL
            | BEGIN statements AGAIN
            | BEGIN statements WHILE statements REPEAT"""
    if p[3].lower() == 'until':
        p[0] = node.BeginUntil(p[2])
    elif p[3].lower() == 'again':
        p[0] = node.BeginAgain(p[2])
    elif p[5] == 'repeat':
        p[0] = node.BeginWhileRepeat(p[2], p[4])
    else:
        p[0] = node.Loop(p[2], p[3])


def p_conditional(p):
    """
    conditional : IF statements THEN
                | IF statements ELSE statements THEN
    """
    if len(p) == 4:
        p[0] = node.Conditional(p[2])
    else:
        p[0] = node.Conditional(p[2], p[4])


def p_function(p):
    """
    function : ':' WORD '(' arguments DOUBLE_HIFEN WORD ')' statements ';'
             | ':' WORD statements ';'
    """
    global functions
    
    if p[2] in functions.keys():
        print(f"Error: Two functions declared with the same name: {p[2]}", file=sys.stderr)
        sys.exit(0)
    else:
        # p[0] = node.Node()
        if len(p) > 5:
            p[0] = node.Function(p[2], p[8], len(p[4]))
        else:
            p[0] = node.Function(p[2], p[3])

        functions[p[2]] = p[0]


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
    p[0] = node.Operation(p[1], previous_num)


def p_comparison(p):
    """comparison : COMPARISON"""
    p[0] = node.Comparison(p[1], previous_num)


def p_num(p):
    """
    num : INT
        | FLOAT
    """
    p[0] = node.Num(p[1])
    global previous_num
    previous_num = p[0].type


def p_words(p):
    """
    words : WORD
    """
    global functions, variables

    if p[1] in functions:
        p[0] = node.Word(p[1], functions[p[1]])
    elif p[1] in variables:
        p[0] = node.Word(p[1])
        variables[p[1]].append(p[0])


def p_forth_function(p):
    """
    forth_function : DOT
                   | DOT_QUOTE
                   | CHAR
                   | EMIT
                   | DUP
                   | SWAP
                   | CR
                   | DROP
                   | ROT
                   | INC_VAR
                   | SPACE
                   | OVER
                   | '!'
                   | '@'
                   | '?'
    """
    p[0] = node.ForthFunction(p.slice[1].type, p.slice[1].value)


def p_error(p):
    print('Erro sintático: ' + str(p))
    parser.exito = False


parser = yacc.yacc()

with open(sys.argv[1], 'r') as forth_file:
    ast = parser.parse(forth_file.read())
