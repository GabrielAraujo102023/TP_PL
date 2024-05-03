class Node:
    def __init__(self):
        pass

    def vm_code(self):
        return ''

    def __str__(self):
        return self.print_tree()

    def print_tree(self, depth=0):
        indent = '  ' * depth
        tree_str = indent + self.__class__.__name__ + '\n'
        for attr, value in self.__dict__.items():
            if isinstance(value, Node):
                tree_str += value.print_tree(depth + 1)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, Node):
                        tree_str += item.print_tree(depth + 1)
                    else:
                        tree_str += indent + '  ' + str(item) + '\n'
            else:
                tree_str += indent + '  ' + str(attr) + ': ' + str(value) + '\n'
        return tree_str


class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def vm_code(self):
        code = "START\n"
        for statement in self.statements:
            if isinstance(statement, Function):
                continue
            code += statement.vm_code()
        return code + "STOP\n"


class Statement(Node):
    def __init__(self, value=None):
        self.value = value

    def vm_code(self):
        return self.value.vm_code()


class Function(Node):
    def __init__(self, word, function_body, arguments=None):
        self.word = word
        self.arguments = arguments
        self.function_body = function_body

    def vm_code(self):
        # arguments_str = ' '.join(self.arguments) if self.arguments else ''
        res = f"{self.word}:\n"
        if self.arguments:
            for i in range(-1, -self.arguments - 1, -1):
                res += f"pushfp\nload {i}\n"
        res += self.function_body.vm_code()
        if self.arguments:
            res += f"storeg {self.arguments}\n"
        return res + 'return'


class FunctionBody(Node):
    def __init__(self, statements):
        self.statements = statements

    def vm_code(self):
        code = ""
        for statement in self.statements:
            code += statement.vm_code()
        return code


class Num(Node):
    def __init__(self, value):
        self.value = value
        self.type = type(value).__name__

    def vm_code(self):
        res = ''
        if isinstance(self.value, int):
            res += f"pushi {self.value}"
        elif isinstance(self.value, float):
            res += f"pushf {self.value}"
        return res + '\n'


class Word(Node):
    def __init__(self, value, function=None):
        self.value = value
        self.function = function

    def vm_code(self):
        res = ''
        if self.function:
            args = self.function.arguments
            if args:
                for i in range(args):
                    res += f'storeg {i}\n'
                for i in range(args):
                    res += f'pushg {i}\n'
            res += f"pusha {self.value}\ncall" #\npop {args}\npushg {args}
        else:
            res += f"pushs {self.value}"
        return res + '\n'


class ConditionConstruct(Node):
    def __init__(self, condition, true_statements, if_number, false_statements=None):
        self.condition = condition
        self.true_statements = true_statements
        self.false_statements = false_statements
        self.if_number = if_number

    def vm_code(self):
        code = self.condition.vm_code()
        code += "jz else1\n"
        for statement in self.true_statements:
            code += statement.vm_code()
        code += "jump endif1\nelse1:"
        for statement in self.false_statements:
            code += statement.vm_code()
        code += "endif1:"
        return code + '\n'


class ForthFunction(Node):
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def vm_code(self):
        res = ''
        match self.type:
            case 'DOT': res = 'writei'
            case 'DOT_QUOTE': res = 'pushs "' + self.value + '"\nwrites'
            case 'EMIT': res = 'writechr'
            case 'CHAR': res = 'pushs "' + self.value + '"\nchrcode'
            case 'DUP': res = f'dup {self.value}'
            case 'SWAP': res = 'swap'
            case 'CR': res = 'writeln'
            case 'DROP': res = f'pop {self.value}'
        return res + '\n'


class Operation(Node):
    def __init__(self, operator, op_type):
        self.operator = operator
        self.operand_type = op_type

    def vm_code(self):
        match self.operator:
            case '+':
                if self.operand_type == "float":
                    res = 'fadd'
                else:
                    res = 'add'
            case '-':
                if self.operand_type == "float":
                    res = 'fsub'
                else:
                    res = 'sub'
            case '*':
                if self.operand_type == "float":
                    res = 'fmul'
                else:
                    res = 'mul'
            case '/':
                if self.operand_type == "float":
                    res = 'fdiv'
                else:
                    res = 'div'
            case 'mod': res = 'mod'
            case 'negate': res = 'pushi -1\nmul'

        return res + '\n'


class Comparison(Node):
    def __init__(self, operator, op_type):
        self.operator = operator
        self.op_type = op_type

    def vm_code(self):
        match self.operator:
            case '>':
                if self.op_type == "float":
                    res = 'fsup'
                else:
                    res = 'sup'
            case '<':
                if self.op_type == 'float':
                    res = 'finf'
                else:
                    res = 'inf'
            case '=': res = 'equal'

        return res + '\n'
