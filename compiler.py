import node
from parser import ast, functions, variables
import sys

if len(sys.argv) != 2:
    print('Erro: Introduza path a um ficheiro com código FORTH.', file=sys.stderr)
    sys.exit(-1)

def process_ast(nodes, rp=0, cc=0, lc=0, sp=0):
    for n in nodes:
        if isinstance(n, node.Function):
            rp, cc, lc, sp = process_ast(n.statements, rp, cc, lc, sp)
        elif isinstance(n, node.Conditional):
            n.conditional_id = cc
            cc += 1
            rp, cc, lc, sp = process_ast(n.true_statements, rp, cc, lc, sp)
            if n.false_statements:
                rp, cc, lc, sp = process_ast(n.false_statements, rp, cc, lc, sp)
        elif isinstance(n, node.Loop):
            n.loop_id = lc
            n.index_p = rp
            rp += 1
            n.limit_p = rp
            rp += 1
            lc += 1
            rp, cc, lc, sp = process_ast(n.statements, rp, cc, lc, sp)
        elif isinstance(n, node.BeginUntil) or isinstance(n, node.BeginAgain):
            n.loop_id = lc
            lc += 1
            rp, cc, lc, sp = process_ast(n.statements, rp, cc, lc, sp)
        elif isinstance(n, node.BeginWhileRepeat):
            n.loop_id = lc
            lc += 1
            rp, cc, lc, sp = process_ast(n.conditions, rp, cc, lc, sp)
            rp, cc, lc, sp = process_ast(n.statements, rp, cc, lc, sp)
        elif isinstance(n, node.Word) and n.value in variables:
            if variables[n.value][1].sp is not None:
                n.sp = variables[n.value][1].sp
            else:
                n.sp = sp
                variables[n.value][1].sp = sp
                sp += 1
            n.is_constant = isinstance(variables[n.value][0], node.Constant)
        elif isinstance(n, node.ForthFunction):
            if n.name == 'INC_VAR':
                n.value = rp
                rp += 1
            elif n.name == 'ROT':
                n.value = rp
                rp += 1
    return rp, cc, lc, sp


total_vars, _, _, _ = process_ast(ast.__dict__['statements'])
# print(ast)

program_code = ast.vm_code()
functions_code = ""

for func in functions.values():
    functions_code += func.vm_code()

push_vars = ""
if total_vars > 0:
    push_vars += f"pushn {total_vars}\n\n"

vm_code = push_vars + program_code + functions_code
print(vm_code)
