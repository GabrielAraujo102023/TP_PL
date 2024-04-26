
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARITHMETIC_OP CHAR DOT DOT_QUOTE DOUBLE_HIFEN EMIT NUMBER WORDprogram : statementsstatements : statement\n                  | statement statementsstatement : function\n                 | expression\n                 | default_functionfunction : ':' WORD '(' arguments DOUBLE_HIFEN WORD ')' function_body ';'\n                | ':' WORD function_body ';'function_body : statements\n    arguments : arguments WORD\n              | WORD\n    expression : literal\n                  | operationliteral : NUMBER\n               | WORDoperation : ARITHMETIC_OPdefault_function : DOT\n                        | DOT_QUOTE\n                        | CHAR\n                        | EMIT"
    
_lr_action_items = {':':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[7,7,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,7,-8,7,-7,]),'DOT':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[11,11,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,11,-8,11,-7,]),'DOT_QUOTE':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[12,12,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,12,-8,12,-7,]),'CHAR':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[13,13,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,13,-8,13,-7,]),'EMIT':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[14,14,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,14,-8,14,-7,]),'NUMBER':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[15,15,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,15,-8,15,-7,]),'WORD':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,22,23,24,25,26,28,30,],[8,8,-4,-5,-6,18,-15,-12,-13,-17,-18,-19,-20,-14,-16,8,22,-11,25,-8,-10,27,8,-7,]),'ARITHMETIC_OP':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,18,24,28,30,],[16,16,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,16,-8,16,-7,]),'$end':([1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,24,30,],[0,-1,-2,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,-3,-8,-7,]),';':([3,4,5,6,8,9,10,11,12,13,14,15,16,17,20,21,24,29,30,],[-2,-4,-5,-6,-15,-12,-13,-17,-18,-19,-20,-14,-16,-3,24,-9,-8,30,-7,]),'(':([18,],[19,]),'DOUBLE_HIFEN':([22,23,25,],[-11,26,-10,]),')':([27,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,3,18,28,],[2,17,21,21,]),'statement':([0,3,18,28,],[3,3,3,3,]),'function':([0,3,18,28,],[4,4,4,4,]),'expression':([0,3,18,28,],[5,5,5,5,]),'default_function':([0,3,18,28,],[6,6,6,6,]),'literal':([0,3,18,28,],[9,9,9,9,]),'operation':([0,3,18,28,],[10,10,10,10,]),'function_body':([18,28,],[20,29,]),'arguments':([19,],[23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parserv2.py',15),
  ('statements -> statement','statements',1,'p_statements','parserv2.py',20),
  ('statements -> statement statements','statements',2,'p_statements','parserv2.py',21),
  ('statement -> function','statement',1,'p_statement','parserv2.py',29),
  ('statement -> expression','statement',1,'p_statement','parserv2.py',30),
  ('statement -> default_function','statement',1,'p_statement','parserv2.py',31),
  ('function -> : WORD ( arguments DOUBLE_HIFEN WORD ) function_body ;','function',9,'p_function','parserv2.py',36),
  ('function -> : WORD function_body ;','function',4,'p_function','parserv2.py',37),
  ('function_body -> statements','function_body',1,'p_function_body','parserv2.py',54),
  ('arguments -> arguments WORD','arguments',2,'p_arguments','parserv2.py',60),
  ('arguments -> WORD','arguments',1,'p_arguments','parserv2.py',61),
  ('expression -> literal','expression',1,'p_expression','parserv2.py',70),
  ('expression -> operation','expression',1,'p_expression','parserv2.py',71),
  ('literal -> NUMBER','literal',1,'p_literal','parserv2.py',76),
  ('literal -> WORD','literal',1,'p_literal','parserv2.py',77),
  ('operation -> ARITHMETIC_OP','operation',1,'p_operation','parserv2.py',82),
  ('default_function -> DOT','default_function',1,'p_default_function','parserv2.py',87),
  ('default_function -> DOT_QUOTE','default_function',1,'p_default_function','parserv2.py',88),
  ('default_function -> CHAR','default_function',1,'p_default_function','parserv2.py',89),
  ('default_function -> EMIT','default_function',1,'p_default_function','parserv2.py',90),
]
