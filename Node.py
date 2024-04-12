class Node:
    def __init__(self):
        pass

class S(Node):
    def __init__(self, expression):
        self.expression = expression

    def vm_code(self):
        return self.expression.vm_code()

class Expression(Node):
    def __init__(self, type, expression1,  expression2, other):
        self.type = type
        self.expression1 = expression1
        self.expression2 = expression2
        self.other = other

    def vm_code(self):
        return self.expression1.vm_code() + self.expression2.vm_code() + self.other.vm_code()

class ArithmeticOperation(Node):
    def __init__(self, type):
        self.type = type

    def vm_code(self):
        res = ''
        if self.type == '+':
            res = 'ADD'
        elif self.type == '-':
            res = 'SUB'
        elif self.type == '/':
            res = 'DIV'
        elif self.type == '*':
            res = 'MUL'
        elif self.type == 'NEGATE':
            res = '-1 MUL'

        return res + '\n'

class Number(Node):
    def __init__(self, number):
        self.number = number

    def vm_code(self):
        return f'PUSHI {self.number}\n'