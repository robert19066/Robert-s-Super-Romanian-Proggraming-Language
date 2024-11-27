
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACOLADA_DREAPTA ACOLADA_STANGA AFISEAZA ALTEL DACA EGAL ID IMPARTE INMULTESTE INTRARE MARE MIC MINUS NUMAR PARANTEZA_DREAPTA PARANTEZA_STANGA PLUS SAU SI STRINGprogram : statement\n               | statement programstatement : ID EGAL expressionstatement : AFISEAZA expressionstatement : INTRARE IDstatement : DACA expression block\n                 | DACA expression block ALTEL blockblock : ACOLADA_STANGA program ACOLADA_DREAPTAexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression INMULTESTE expression\n                  | expression IMPARTE expression\n                  | expression MARE expression\n                  | expression MIC expression\n                  | expression SI expression\n                  | expression SAU expressionexpression : PARANTEZA_STANGA expression PARANTEZA_DREAPTAexpression : NUMARexpression : STRINGexpression : ID'
    
_lr_action_items = {'ID':([0,2,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,39,40,],[3,3,13,14,13,13,-4,13,-18,-19,-20,-5,-3,13,13,13,13,13,13,13,13,-6,3,-9,-10,-11,-12,-13,-14,-15,-16,-17,-7,-8,]),'AFISEAZA':([0,2,9,11,12,13,14,16,26,27,28,29,30,31,32,33,34,35,36,39,40,],[4,4,-4,-18,-19,-20,-5,-3,-6,4,-9,-10,-11,-12,-13,-14,-15,-16,-17,-7,-8,]),'INTRARE':([0,2,9,11,12,13,14,16,26,27,28,29,30,31,32,33,34,35,36,39,40,],[5,5,-4,-18,-19,-20,-5,-3,-6,5,-9,-10,-11,-12,-13,-14,-15,-16,-17,-7,-8,]),'DACA':([0,2,9,11,12,13,14,16,26,27,28,29,30,31,32,33,34,35,36,39,40,],[6,6,-4,-18,-19,-20,-5,-3,-6,6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-7,-8,]),'$end':([1,2,7,9,11,12,13,14,16,26,28,29,30,31,32,33,34,35,36,39,40,],[0,-1,-2,-4,-18,-19,-20,-5,-3,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-7,-8,]),'ACOLADA_DREAPTA':([2,7,9,11,12,13,14,16,26,28,29,30,31,32,33,34,35,36,38,39,40,],[-1,-2,-4,-18,-19,-20,-5,-3,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,40,-7,-8,]),'EGAL':([3,],[8,]),'PARANTEZA_STANGA':([4,6,8,10,17,18,19,20,21,22,23,24,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'NUMAR':([4,6,8,10,17,18,19,20,21,22,23,24,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'STRING':([4,6,8,10,17,18,19,20,21,22,23,24,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'PLUS':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[17,-18,-19,-20,17,17,17,17,17,17,17,17,17,17,17,-17,]),'MINUS':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[18,-18,-19,-20,18,18,18,18,18,18,18,18,18,18,18,-17,]),'INMULTESTE':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[19,-18,-19,-20,19,19,19,19,19,19,19,19,19,19,19,-17,]),'IMPARTE':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[20,-18,-19,-20,20,20,20,20,20,20,20,20,20,20,20,-17,]),'MARE':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[21,-18,-19,-20,21,21,21,21,21,21,21,21,21,21,21,-17,]),'MIC':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[22,-18,-19,-20,22,22,22,22,22,22,22,22,22,22,22,-17,]),'SI':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[23,-18,-19,-20,23,23,23,23,23,23,23,23,23,23,23,-17,]),'SAU':([9,11,12,13,15,16,25,28,29,30,31,32,33,34,35,36,],[24,-18,-19,-20,24,24,24,24,24,24,24,24,24,24,24,-17,]),'ACOLADA_STANGA':([11,12,13,15,28,29,30,31,32,33,34,35,36,37,],[-18,-19,-20,27,-9,-10,-11,-12,-13,-14,-15,-16,-17,27,]),'PARANTEZA_DREAPTA':([11,12,13,25,28,29,30,31,32,33,34,35,36,],[-18,-19,-20,36,-9,-10,-11,-12,-13,-14,-15,-16,-17,]),'ALTEL':([26,40,],[37,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,27,],[1,7,38,]),'statement':([0,2,27,],[2,2,2,]),'expression':([4,6,8,10,17,18,19,20,21,22,23,24,],[9,15,16,25,28,29,30,31,32,33,34,35,]),'block':([15,37,],[26,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','src.py',73),
  ('program -> statement program','program',2,'p_program','src.py',74),
  ('statement -> ID EGAL expression','statement',3,'p_statement_assign','src.py',81),
  ('statement -> AFISEAZA expression','statement',2,'p_statement_afiseaza','src.py',85),
  ('statement -> INTRARE ID','statement',2,'p_statement_intrare','src.py',89),
  ('statement -> DACA expression block','statement',3,'p_statement_daca','src.py',93),
  ('statement -> DACA expression block ALTEL block','statement',5,'p_statement_daca','src.py',94),
  ('block -> ACOLADA_STANGA program ACOLADA_DREAPTA','block',3,'p_block','src.py',101),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','src.py',105),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','src.py',106),
  ('expression -> expression INMULTESTE expression','expression',3,'p_expression_binop','src.py',107),
  ('expression -> expression IMPARTE expression','expression',3,'p_expression_binop','src.py',108),
  ('expression -> expression MARE expression','expression',3,'p_expression_binop','src.py',109),
  ('expression -> expression MIC expression','expression',3,'p_expression_binop','src.py',110),
  ('expression -> expression SI expression','expression',3,'p_expression_binop','src.py',111),
  ('expression -> expression SAU expression','expression',3,'p_expression_binop','src.py',112),
  ('expression -> PARANTEZA_STANGA expression PARANTEZA_DREAPTA','expression',3,'p_expression_group','src.py',116),
  ('expression -> NUMAR','expression',1,'p_expression_numar','src.py',120),
  ('expression -> STRING','expression',1,'p_expression_string','src.py',124),
  ('expression -> ID','expression',1,'p_expression_id','src.py',128),
]
