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
                continue  # Skip functions
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
        return f"{self.word}:\n{self.function_body.vm_code()}return"


class FunctionBody(Node):
    def __init__(self, statements):
        self.statements = statements

    def vm_code(self):
        code = ""
        for statement in self.statements:
            code += statement.vm_code()
        return code


class Literal(Node):
    def __init__(self, value, function=None):
        self.value = value
        self.function = function

    def vm_code(self):
        res = ''
        if isinstance(self.value, int):
            res += f"pushi {self.value}\n"
        elif self.function:
            args = self.function.arguments
            for i in range(args):
                res += f'storeg {i}\n'
            for i in range(args):
                res += f'pushg {i}\n'
            res += f"pusha {self.value}\ncall\npop {args}\npushg {args}\n"
        else:
            res += f"pushs {self.value}\n"

        return res


class DefaultFunction(Node):
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
        return res + '\n'


class Operation(Node):
    def __init__(self, operator):
        self.operator = operator

    def vm_code(self):
        res = ''
        match self.operator:
            case '+': res = 'add'
            case '-': res = 'sub'
            case '*': res = 'mul'
            case '/': res = 'div'
        return res + '\n'
