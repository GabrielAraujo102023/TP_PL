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
        super().__init__()
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
        super().__init__()
        self.value = value

    def vm_code(self):
        return self.value.vm_code()


class Function(Node):
    def __init__(self, word, statements, arguments=None):
        super().__init__()
        self.word = word
        self.arguments = arguments
        self.args_sp = None
        self.statements = statements

    def vm_code(self):
        res = f"\n{self.word}:\n"
        if self.arguments:
            if self.arguments == 1:
                res += f"pushst {self.args_sp}\nload 0\n"
            else:
                for i in range(self.arguments - 1, - 1, -1):
                    res += f"pushst {self.args_sp}\nload {i}\n"

        for statement in self.statements:
            res += statement.vm_code()

        return res + 'return\n'


class Num(Node):
    def __init__(self, value):
        super().__init__()
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
        super().__init__()
        self.value = value
        self.function = function
        self.sp = None
        self.is_constant = None

    def vm_code(self):
        res = ''
        if self.function:
            f = self.function
            if f.arguments:
                for i in range(f.arguments):
                    res += f"pushst {f.args_sp}\nswap\nstore {i}\n"
            res += f"pusha {self.value}\ncall"
        elif self.sp is not None:
            res += f"pushst {self.sp}"
            if self.is_constant:
                res += f'\nload 0'
        return res + '\n'


class Variable(Node):
    def __init__(self, variable_id):
        super().__init__()
        self.variable_id = variable_id
        self.sp = None

    def vm_code(self):
        res = 'alloc 1\npushi 0\nstore 0'
        return res + '\n'


class Constant(Node):
    def __init__(self, constant_id):
        super().__init__()
        self.constant_id = constant_id
        self.sp = None

    def vm_code(self):
        res = 'alloc 1\nswap\nstore 0'
        return res + '\n'


class Conditional(Node):
    def __init__(self, true_statements, false_statements=None):
        super().__init__()
        self.conditional_id = None
        self.true_statements = true_statements
        self.false_statements = false_statements

    def vm_code(self):
        code = f"jz else{self.conditional_id}\n"
        for statement in self.true_statements:
            code += statement.vm_code()
        code += f"jump endif{self.conditional_id}\nelse{self.conditional_id}:\n"
        if self.false_statements:
            for statement in self.false_statements:
                code += statement.vm_code()
        code += f"endif{self.conditional_id}:"
        return code + '\n'


class Loop(Node):
    def __init__(self, statements, loop_type):
        super().__init__()
        self.loop_id = None
        self.loop_type = loop_type
        self.limit_p = None
        self.index_p = None
        self.statements = statements

    def vm_code(self):
        res = f"storeg {self.index_p}\nstoreg {self.limit_p}\nwhile{self.loop_id}:\npushg {self.index_p}\npushg {self.limit_p}\ninf\njz endwhile{self.loop_id}\n"
        for statement in self.statements:
            res += statement.vm_code()
        if self.loop_type == 'loop':
            res += f"pushg {self.index_p}\npushi 1\nadd\nstoreg {self.index_p}\njump while{self.loop_id}\nendwhile{self.loop_id}:"
        else:
            res += f"pushg {self.index_p}\nadd\nstoreg {self.index_p}\njump while{self.loop_id}\nendwhile{self.loop_id}:"

        return res + '\n'


class BeginUntil(Node):
    def __init__(self, statements):
        super().__init__()
        self.loop_id = None
        self.statements = statements

    def vm_code(self):
        res = f"pushi 1\nwhile{self.loop_id}:\njz endwhile{self.loop_id}\n"
        for statement in self.statements:
            res += statement.vm_code()

        res += f"not\njump while{self.loop_id}\nendwhile{self.loop_id}:"

        return res + '\n'


class BeginAgain(Node):
    def __init__(self, statements):
        super().__init__()
        self.loop_id = None
        self.statements = statements

    def vm_code(self):
        res = f"while{self.loop_id}:\npushi 1\njz endwhile{self.loop_id}\n"
        for statement in self.statements:
            res += statement.vm_code()

        res += f"jump while{self.loop_id}\nendwhile{self.loop_id}:"

        return res + '\n'


class BeginWhileRepeat(Node):
    def __init__(self, conditions, statements):
        super().__init__()
        self.loop_id = None
        self.conditions = conditions
        self.statements = statements

    def vm_code(self):
        res = f"while{self.loop_id}:\n"

        for conditions in self.conditions:
            res += conditions.vm_code()

        res += f"jz endwhile{self.loop_id}\n"

        for statement in self.statements:
            res += statement.vm_code()

        res += f"jump while{self.loop_id}\nendwhile{self.loop_id}:"

        return res + '\n'


class ForthFunction(Node):
    def __init__(self, name, value=None):
        super().__init__()
        self.name = name
        self.value = value

    def vm_code(self):
        res = ''
        match self.name:
            case 'DOT':
                res = 'writei pushs " " writes'
            case 'DOT_QUOTE':
                res = 'pushs "' + self.value + '"\nwrites'
            case 'EMIT':
                res = 'writechr'
            case 'CHAR':
                res = 'pushs "' + self.value + '"\nchrcode'
            case 'DUP':
                if self.value == 1:
                    res = f'dup {self.value}'
                else:
                    res = 'pushsp\nload -1\npushsp\nload -1'
            case 'SWAP':
                res = 'swap'
            case 'OVER':
                if self.value == 1:
                    res = 'pushsp\nload -1'
                else:
                    res = 'pushsp\nload -3\npushsp\nload -3'
            case 'CR':
                res = 'writeln'
            case 'DROP':
                res = f'pop {self.value}'
            case 'ROT':
                res = f'storeg {self.value}\nswap\npushg {self.value}\nswap'
            case 'SPACE':
                res = 'pushs " " writes'
            case '!':
                res = 'swap\nstore 0'
            case '@':
                res = 'load 0'
            case '?':
                res = 'load 0\nwritei pushs " " writes'
            case 'INC_VAR':
                res = f'swap\nstoreg {self.value}\npushi 1\ndupn\nload 0\npushg {self.value}\nadd\nstore 0'
        return res + '\n'


class Operation(Node):
    def __init__(self, operator, op_type):
        super().__init__()
        self.operator = operator
        self.operand_type = op_type

    def vm_code(self):
        res = ''
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
            case 'mod':
                res = 'mod'
            case 'negate':
                res = 'pushi -1\nmul'

        return res + '\n'


class Comparison(Node):
    def __init__(self, operator, op_type):
        super().__init__()
        self.operator = operator
        self.op_type = op_type

    def vm_code(self):
        res = ''
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
            case '=':
                res = 'equal'
            case '<>':
                res = 'equal\nnot'
            case '0=':
                res = 'not'
            case '0<':
                res = 'pushi 0\ninf'
            case '0>':
                res = 'pushi 0\nsup'
            case 'and':
                res = 'and'
            case 'or':
                res = 'or'

        return res + '\n'
