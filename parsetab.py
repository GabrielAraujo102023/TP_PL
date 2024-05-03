
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARITHMETIC_OP CHAR COMPARISON CR DOT DOT_QUOTE DOUBLE_HIFEN DROP DUP ELSE EMIT FLOAT IF INT KEY SWAP THEN WORDprogram : statements\n    statements : statement\n               | statement statements\n    \n    statement : function\n              | condition_construct\n              | operation\n              | comparison\n              | forth_function\n              | words\n              | num\n    \n    condition_construct : comparison IF statements THEN\n                        | comparison IF statements ELSE statements THEN\n    \n    function : ':' WORD '(' arguments DOUBLE_HIFEN WORD ')' function_body ';'\n             | ':' WORD function_body ';'\n    function_body : statements\n    arguments : arguments WORD\n              | WORD\n    operation : ARITHMETIC_OPcomparison : COMPARISON\n    num : INT\n        | FLOAT\n    \n    words : WORD\n    \n    forth_function : DOT\n                   | DOT_QUOTE\n                   | CHAR\n                   | EMIT\n                   | DUP\n                   | SWAP\n                   | CR\n                   | KEY\n                   | DROP\n    "
    
_lr_action_items = {':':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[11,11,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,11,11,-11,11,-14,-12,11,-13,]),'ARITHMETIC_OP':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[13,13,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,13,13,-11,13,-14,-12,13,-13,]),'COMPARISON':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[14,14,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,14,14,-11,14,-14,-12,14,-13,]),'DOT':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[15,15,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,15,15,-11,15,-14,-12,15,-13,]),'DOT_QUOTE':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[16,16,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,16,16,-11,16,-14,-12,16,-13,]),'CHAR':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[17,17,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,17,17,-11,17,-14,-12,17,-13,]),'EMIT':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[18,18,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,18,18,-11,18,-14,-12,18,-13,]),'DUP':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[19,19,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,19,19,-11,19,-14,-12,19,-13,]),'SWAP':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[20,20,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,20,20,-11,20,-14,-12,20,-13,]),'CR':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[21,21,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,21,21,-11,21,-14,-12,21,-13,]),'KEY':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[22,22,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,22,22,-11,22,-14,-12,22,-13,]),'DROP':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[23,23,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,23,23,-11,23,-14,-12,23,-13,]),'WORD':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,30,33,34,35,36,37,39,40,41,43,45,],[12,12,-4,-5,-6,-7,-8,-9,-10,28,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,12,12,35,-11,12,-17,39,-14,-16,42,-12,12,-13,]),'INT':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[24,24,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,24,24,-11,24,-14,-12,24,-13,]),'FLOAT':([0,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,33,34,37,41,43,45,],[25,25,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,25,25,-11,25,-14,-12,25,-13,]),'$end':([1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,33,37,41,45,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,-3,-11,-14,-12,-13,]),'THEN':([3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,33,37,38,41,45,],[-2,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,-3,33,-11,-14,41,-12,-13,]),'ELSE':([3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,33,37,41,45,],[-2,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,-3,34,-11,-14,-12,-13,]),';':([3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,31,32,33,37,41,44,45,],[-2,-4,-5,-6,-7,-8,-9,-10,-22,-18,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-20,-21,-3,37,-15,-11,-14,-12,45,-13,]),'IF':([7,14,],[27,-19,]),'(':([28,],[30,]),'DOUBLE_HIFEN':([35,36,39,],[-17,40,-16,]),')':([42,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,3,27,28,34,43,],[2,26,29,32,38,32,]),'statement':([0,3,27,28,34,43,],[3,3,3,3,3,3,]),'function':([0,3,27,28,34,43,],[4,4,4,4,4,4,]),'condition_construct':([0,3,27,28,34,43,],[5,5,5,5,5,5,]),'operation':([0,3,27,28,34,43,],[6,6,6,6,6,6,]),'comparison':([0,3,27,28,34,43,],[7,7,7,7,7,7,]),'forth_function':([0,3,27,28,34,43,],[8,8,8,8,8,8,]),'words':([0,3,27,28,34,43,],[9,9,9,9,9,9,]),'num':([0,3,27,28,34,43,],[10,10,10,10,10,10,]),'function_body':([28,43,],[31,44,]),'arguments':([30,],[36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parserv2.py',19),
  ('statements -> statement','statements',1,'p_statements','parserv2.py',25),
  ('statements -> statement statements','statements',2,'p_statements','parserv2.py',26),
  ('statement -> function','statement',1,'p_statement','parserv2.py',36),
  ('statement -> condition_construct','statement',1,'p_statement','parserv2.py',37),
  ('statement -> operation','statement',1,'p_statement','parserv2.py',38),
  ('statement -> comparison','statement',1,'p_statement','parserv2.py',39),
  ('statement -> forth_function','statement',1,'p_statement','parserv2.py',40),
  ('statement -> words','statement',1,'p_statement','parserv2.py',41),
  ('statement -> num','statement',1,'p_statement','parserv2.py',42),
  ('condition_construct -> comparison IF statements THEN','condition_construct',4,'p_condition_construct','parserv2.py',49),
  ('condition_construct -> comparison IF statements ELSE statements THEN','condition_construct',6,'p_condition_construct','parserv2.py',50),
  ('function -> : WORD ( arguments DOUBLE_HIFEN WORD ) function_body ;','function',9,'p_function','parserv2.py',63),
  ('function -> : WORD function_body ;','function',4,'p_function','parserv2.py',64),
  ('function_body -> statements','function_body',1,'p_function_body','parserv2.py',84),
  ('arguments -> arguments WORD','arguments',2,'p_arguments','parserv2.py',90),
  ('arguments -> WORD','arguments',1,'p_arguments','parserv2.py',91),
  ('operation -> ARITHMETIC_OP','operation',1,'p_operation','parserv2.py',101),
  ('comparison -> COMPARISON','comparison',1,'p_comparison','parserv2.py',106),
  ('num -> INT','num',1,'p_num','parserv2.py',112),
  ('num -> FLOAT','num',1,'p_num','parserv2.py',113),
  ('words -> WORD','words',1,'p_words','parserv2.py',122),
  ('forth_function -> DOT','forth_function',1,'p_forth_function','parserv2.py',133),
  ('forth_function -> DOT_QUOTE','forth_function',1,'p_forth_function','parserv2.py',134),
  ('forth_function -> CHAR','forth_function',1,'p_forth_function','parserv2.py',135),
  ('forth_function -> EMIT','forth_function',1,'p_forth_function','parserv2.py',136),
  ('forth_function -> DUP','forth_function',1,'p_forth_function','parserv2.py',137),
  ('forth_function -> SWAP','forth_function',1,'p_forth_function','parserv2.py',138),
  ('forth_function -> CR','forth_function',1,'p_forth_function','parserv2.py',139),
  ('forth_function -> KEY','forth_function',1,'p_forth_function','parserv2.py',140),
  ('forth_function -> DROP','forth_function',1,'p_forth_function','parserv2.py',141),
]
