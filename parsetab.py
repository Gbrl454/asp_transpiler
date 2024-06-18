
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEITHERORleftPLUSMINUSleftTIMESDIVIDEMODBYrightEQUALSBOOLEAN BY CHARCONST COLON COMMA DIVIDE DO DOT EITHER END EQ EQUALS FLOAT FOR FUNCTION GET GT GTE HAVING IDENTIFIER IN INT LBRACE LPAREN LT LTE MINUS MOD NEQ NULL NUMBER OR PLUS RBRACE RETURN RPAREN SEMICOLON SHOW TEXT TIMES TYPE VARprint_statement : SHOW expression SEMICOLONexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | term MOD factor\n            | factorfactor : NUMBER\n              | FLOAT\n              | CHARCONST\n              | LPAREN expression RPAREN\n              | designatordesignator : IDENTIFIER\n                  | designator DOT IDENTIFIERtype : INT\n            | BOOLEAN\n            | TEXT\n            | FLOAT\n            | IDENTIFIERexpression : NULL'
    
_lr_action_items = {'SHOW':([0,],[2,]),'$end':([1,13,],[0,-1,]),'NULL':([2,10,],[5,5,]),'NUMBER':([2,10,14,15,16,17,18,],[7,7,7,7,7,7,7,]),'FLOAT':([2,10,14,15,16,17,18,],[8,8,8,8,8,8,8,]),'CHARCONST':([2,10,14,15,16,17,18,],[9,9,9,9,9,9,9,]),'LPAREN':([2,10,14,15,16,17,18,],[10,10,10,10,10,10,10,]),'IDENTIFIER':([2,10,14,15,16,17,18,20,],[12,12,12,12,12,12,12,27,]),'SEMICOLON':([3,4,5,6,7,8,9,11,12,21,22,23,24,25,26,27,],[13,-4,-21,-8,-9,-10,-11,-13,-14,-2,-3,-5,-6,-7,-12,-15,]),'PLUS':([3,4,5,6,7,8,9,11,12,19,21,22,23,24,25,26,27,],[14,-4,-21,-8,-9,-10,-11,-13,-14,14,-2,-3,-5,-6,-7,-12,-15,]),'MINUS':([3,4,5,6,7,8,9,11,12,19,21,22,23,24,25,26,27,],[15,-4,-21,-8,-9,-10,-11,-13,-14,15,-2,-3,-5,-6,-7,-12,-15,]),'RPAREN':([4,5,6,7,8,9,11,12,19,21,22,23,24,25,26,27,],[-4,-21,-8,-9,-10,-11,-13,-14,26,-2,-3,-5,-6,-7,-12,-15,]),'TIMES':([4,6,7,8,9,11,12,21,22,23,24,25,26,27,],[16,-8,-9,-10,-11,-13,-14,16,16,-5,-6,-7,-12,-15,]),'DIVIDE':([4,6,7,8,9,11,12,21,22,23,24,25,26,27,],[17,-8,-9,-10,-11,-13,-14,17,17,-5,-6,-7,-12,-15,]),'MOD':([4,6,7,8,9,11,12,21,22,23,24,25,26,27,],[18,-8,-9,-10,-11,-13,-14,18,18,-5,-6,-7,-12,-15,]),'DOT':([11,12,27,],[20,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'print_statement':([0,],[1,]),'expression':([2,10,],[3,19,]),'term':([2,10,14,15,],[4,4,21,22,]),'factor':([2,10,14,15,16,17,18,],[6,6,6,6,23,24,25,]),'designator':([2,10,14,15,16,17,18,],[11,11,11,11,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> print_statement","S'",1,None,None,None),
  ('print_statement -> SHOW expression SEMICOLON','print_statement',3,'p_print_statement','parser.py',19),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser.py',24),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser.py',25),
  ('expression -> term','expression',1,'p_expression','parser.py',26),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',36),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',37),
  ('term -> term MOD factor','term',3,'p_term','parser.py',38),
  ('term -> factor','term',1,'p_term','parser.py',39),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',51),
  ('factor -> FLOAT','factor',1,'p_factor','parser.py',52),
  ('factor -> CHARCONST','factor',1,'p_factor','parser.py',53),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',54),
  ('factor -> designator','factor',1,'p_factor','parser.py',55),
  ('designator -> IDENTIFIER','designator',1,'p_designator','parser.py',63),
  ('designator -> designator DOT IDENTIFIER','designator',3,'p_designator','parser.py',64),
  ('type -> INT','type',1,'p_type','parser.py',71),
  ('type -> BOOLEAN','type',1,'p_type','parser.py',72),
  ('type -> TEXT','type',1,'p_type','parser.py',73),
  ('type -> FLOAT','type',1,'p_type','parser.py',74),
  ('type -> IDENTIFIER','type',1,'p_type','parser.py',75),
  ('expression -> NULL','expression',1,'p_null','parser.py',80),
]
