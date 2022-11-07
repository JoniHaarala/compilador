
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSING COMMA COMMENT DECIMAL DIV DOUBLEDOT ENTERO IDENT IGUAL IN LBRACE LBRACKET LOGICO LPAREN MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL NOT OUT PIN PROD PUNTO RBRACE RBRACKET RESTA RPAREN SEMICOLON SINGLEDOT SPACE SUM TEXTO VAR_ASSING and backward begin end foward function left library or procedure right stop tk_else tk_if tk_while var waitbeginend : begin codigo endcodigo : sentencia\n              | sentencia codigosentencia : libreria\n                 | variable\n                 | control\n                 | definicion\n                 | procedimiento\n                 | funcion\n                 | loopdefinicion : var LPAREN IDENT VAR_ASSING tipo RPAREN SEMICOLONvariable : IDENT ASSING tipo SEMICOLONtipo : TEXTO\n            | ENTERO\n            | DECIMAL\n            | LOGICOcontrol : if\n               | ifelse\n               | whileif : tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLONifelse : tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE elseelse : tk_else LBRACE codigo RBRACE SEMICOLONwhile : tk_while LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLONfuncion : function tipo LPAREN argumento RPAREN SEMICOLONprocedimiento : procedure IDENT LPAREN argumento RPAREN SEMICOLONpin : PIN LPAREN ENTERO SPACE conector RPAREN SEMICOLONconector : IN\n                | OUTargumento : argumento\n                | LPAREN IDENT VAR_ASSING tipo RPAREN\n                | emptylibreria : library LPAREN SINGLEDOT TEXTO PUNTO TEXTO SINGLEDOT RPAREN SEMICOLONloop : adelante\n            | atras\n            | izquierda\n            | derecha\n            | esperar\n            | parar\n            | emptyadelante : foward LPAREN RPAREN SEMICOLONatras : backward LPAREN RPAREN SEMICOLONizquierda : left LPAREN RPAREN SEMICOLONderecha : right LPAREN RPAREN SEMICOLONesperar : wait LPAREN ENTERO RPAREN SEMICOLONparar : stop LPAREN RPAREN SEMICOLONexpression : expression SUM term\n                  | expression RESTA term\n                  | term\n                  | tipo\n                  | variable\n       term       : term PROD factor\n                  | term DIV factor\n                  | factorfactor : ENTERO\n              | LPAREN expression RPARENcondicion : expression relacion expression\n                 | NOT expression\n                 | expression logico expressionrelacion : IGUAL\n                | MAYOR\n                | MENOR\n                | MAYOR_IGUAL\n                | MENOR_IGUALlogico : and\n              | orempty :'
    
_lr_action_items = {'begin':([0,],[2,]),'$end':([1,35,],[0,-1,]),'library':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[12,12,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,12,12,-44,-25,-24,-11,-20,-21,-23,-32,12,-22,]),'IDENT':([2,4,5,6,7,8,9,10,11,14,15,16,18,20,21,22,23,24,25,26,39,46,47,59,62,76,78,84,85,88,89,90,91,92,93,94,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[13,13,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,40,-33,-34,-35,-36,-37,-38,-39,56,13,13,13,13,-12,107,13,13,-59,-60,-61,-62,-63,-64,-65,-40,-41,-42,-43,-45,13,13,-44,-25,-24,-11,-20,-21,-23,-32,13,-22,]),'var':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[17,17,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,17,17,-44,-25,-24,-11,-20,-21,-23,-32,17,-22,]),'procedure':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[18,18,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,18,18,-44,-25,-24,-11,-20,-21,-23,-32,18,-22,]),'function':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[19,19,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,19,19,-44,-25,-24,-11,-20,-21,-23,-32,19,-22,]),'tk_if':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[27,27,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,27,27,-44,-25,-24,-11,-20,-21,-23,-32,27,-22,]),'tk_while':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[28,28,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,28,28,-44,-25,-24,-11,-20,-21,-23,-32,28,-22,]),'foward':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[29,29,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,29,29,-44,-25,-24,-11,-20,-21,-23,-32,29,-22,]),'backward':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[30,30,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,30,30,-44,-25,-24,-11,-20,-21,-23,-32,30,-22,]),'left':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[31,31,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,31,31,-44,-25,-24,-11,-20,-21,-23,-32,31,-22,]),'right':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[32,32,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,32,32,-44,-25,-24,-11,-20,-21,-23,-32,32,-22,]),'wait':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[33,33,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,33,33,-44,-25,-24,-11,-20,-21,-23,-32,33,-22,]),'stop':([2,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,76,99,100,101,102,104,111,119,120,124,125,129,135,136,138,139,140,143,],[34,34,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-12,-40,-41,-42,-43,-45,34,34,-44,-25,-24,-11,-20,-21,-23,-32,34,-22,]),'end':([2,3,4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,36,76,99,100,101,102,104,120,124,125,129,135,136,138,139,143,],[-66,35,-2,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-3,-12,-40,-41,-42,-43,-45,-44,-25,-24,-11,-20,-21,-23,-32,-22,]),'RBRACE':([4,5,6,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,36,76,99,100,101,102,104,111,119,120,124,125,126,127,129,135,136,138,139,140,141,143,],[-2,-4,-5,-6,-7,-8,-9,-10,-17,-18,-19,-33,-34,-35,-36,-37,-38,-39,-3,-12,-40,-41,-42,-43,-45,-66,-66,-44,-25,-24,131,132,-11,-20,-21,-23,-32,-66,142,-22,]),'LPAREN':([12,17,27,28,29,30,31,32,33,34,40,41,42,43,44,45,46,47,57,58,59,62,84,85,86,87,88,89,90,91,92,93,94,96,97,],[37,39,46,47,48,49,50,51,52,53,57,58,-13,-14,-15,-16,59,59,78,78,59,59,59,59,59,59,-59,-60,-61,-62,-63,-64,-65,59,59,]),'ASSING':([13,],[38,]),'TEXTO':([19,38,46,47,54,59,62,77,84,85,88,89,90,91,92,93,94,105,123,],[42,42,42,42,75,42,42,42,42,42,-59,-60,-61,-62,-63,-64,-65,121,42,]),'ENTERO':([19,38,46,47,52,59,62,77,84,85,86,87,88,89,90,91,92,93,94,96,97,123,],[43,43,67,67,73,67,67,43,67,67,115,115,-59,-60,-61,-62,-63,-64,-65,115,115,43,]),'DECIMAL':([19,38,46,47,59,62,77,84,85,88,89,90,91,92,93,94,123,],[44,44,44,44,44,44,44,44,44,-59,-60,-61,-62,-63,-64,-65,44,]),'LOGICO':([19,38,46,47,59,62,77,84,85,88,89,90,91,92,93,94,123,],[45,45,45,45,45,45,45,45,45,-59,-60,-61,-62,-63,-64,-65,45,]),'SINGLEDOT':([37,121,],[54,128,]),'SEMICOLON':([42,43,44,45,55,69,70,71,72,74,103,108,109,122,131,132,133,142,],[-13,-14,-15,-16,76,99,100,101,102,104,120,124,125,129,135,138,139,143,]),'SUM':([42,44,45,61,63,64,65,66,67,76,82,95,110,112,113,114,115,116,117,118,],[-13,-15,-16,86,-48,-49,-50,-53,-14,-12,86,86,-55,86,86,-46,-54,-47,-51,-52,]),'RESTA':([42,44,45,61,63,64,65,66,67,76,82,95,110,112,113,114,115,116,117,118,],[-13,-15,-16,87,-48,-49,-50,-53,-14,-12,87,87,-55,87,87,-46,-54,-47,-51,-52,]),'IGUAL':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,88,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'MAYOR':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,89,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'MENOR':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,90,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'MAYOR_IGUAL':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,91,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'MENOR_IGUAL':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,92,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'and':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,93,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'or':([42,44,45,61,63,64,65,66,67,76,110,114,115,116,117,118,],[-13,-15,-16,94,-48,-49,-50,-53,-14,-12,-55,-46,-54,-47,-51,-52,]),'RPAREN':([42,43,44,45,48,49,50,51,53,57,58,60,63,64,65,66,67,68,73,76,79,80,81,82,95,106,110,112,113,114,115,116,117,118,128,130,134,],[-13,-14,-15,-16,69,70,71,72,74,-66,-66,83,-48,-49,-50,-53,-14,98,103,-12,108,-31,109,110,-57,122,-55,-56,-58,-46,-54,-47,-51,-52,133,134,-30,]),'NOT':([46,47,],[62,62,]),'VAR_ASSING':([56,107,],[77,123,]),'PROD':([63,66,67,110,114,115,116,117,118,],[96,-53,-54,-55,96,-54,96,-51,-52,]),'DIV':([63,66,67,110,114,115,116,117,118,],[97,-53,-54,-55,97,-54,97,-51,-52,]),'PUNTO':([75,],[105,]),'LBRACE':([83,98,137,],[111,119,140,]),'tk_else':([131,],[137,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'beginend':([0,],[1,]),'codigo':([2,4,111,119,140,],[3,36,126,127,141,]),'sentencia':([2,4,111,119,140,],[4,4,4,4,4,]),'libreria':([2,4,111,119,140,],[5,5,5,5,5,]),'variable':([2,4,46,47,59,62,84,85,111,119,140,],[6,6,65,65,65,65,65,65,6,6,6,]),'control':([2,4,111,119,140,],[7,7,7,7,7,]),'definicion':([2,4,111,119,140,],[8,8,8,8,8,]),'procedimiento':([2,4,111,119,140,],[9,9,9,9,9,]),'funcion':([2,4,111,119,140,],[10,10,10,10,10,]),'loop':([2,4,111,119,140,],[11,11,11,11,11,]),'if':([2,4,111,119,140,],[14,14,14,14,14,]),'ifelse':([2,4,111,119,140,],[15,15,15,15,15,]),'while':([2,4,111,119,140,],[16,16,16,16,16,]),'adelante':([2,4,111,119,140,],[20,20,20,20,20,]),'atras':([2,4,111,119,140,],[21,21,21,21,21,]),'izquierda':([2,4,111,119,140,],[22,22,22,22,22,]),'derecha':([2,4,111,119,140,],[23,23,23,23,23,]),'esperar':([2,4,111,119,140,],[24,24,24,24,24,]),'parar':([2,4,111,119,140,],[25,25,25,25,25,]),'empty':([2,4,57,58,111,119,140,],[26,26,80,80,26,26,26,]),'tipo':([19,38,46,47,59,62,77,84,85,123,],[41,55,64,64,64,64,106,64,64,130,]),'condicion':([46,47,],[60,68,]),'expression':([46,47,59,62,84,85,],[61,61,82,95,112,113,]),'term':([46,47,59,62,84,85,86,87,],[63,63,63,63,63,63,114,116,]),'factor':([46,47,59,62,84,85,86,87,96,97,],[66,66,66,66,66,66,66,66,117,118,]),'argumento':([57,58,],[79,81,]),'relacion':([61,],[84,]),'logico':([61,],[85,]),'else':([131,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> beginend","S'",1,None,None,None),
  ('beginend -> begin codigo end','beginend',3,'p_body','main.py',8),
  ('codigo -> sentencia','codigo',1,'p_codigo','main.py',11),
  ('codigo -> sentencia codigo','codigo',2,'p_codigo','main.py',12),
  ('sentencia -> libreria','sentencia',1,'p_sentencia','main.py',15),
  ('sentencia -> variable','sentencia',1,'p_sentencia','main.py',16),
  ('sentencia -> control','sentencia',1,'p_sentencia','main.py',17),
  ('sentencia -> definicion','sentencia',1,'p_sentencia','main.py',18),
  ('sentencia -> procedimiento','sentencia',1,'p_sentencia','main.py',19),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','main.py',20),
  ('sentencia -> loop','sentencia',1,'p_sentencia','main.py',21),
  ('definicion -> var LPAREN IDENT VAR_ASSING tipo RPAREN SEMICOLON','definicion',7,'p_definicion','main.py',24),
  ('variable -> IDENT ASSING tipo SEMICOLON','variable',4,'p_variable','main.py',27),
  ('tipo -> TEXTO','tipo',1,'p_tipo','main.py',30),
  ('tipo -> ENTERO','tipo',1,'p_tipo','main.py',31),
  ('tipo -> DECIMAL','tipo',1,'p_tipo','main.py',32),
  ('tipo -> LOGICO','tipo',1,'p_tipo','main.py',33),
  ('control -> if','control',1,'p_control','main.py',38),
  ('control -> ifelse','control',1,'p_control','main.py',39),
  ('control -> while','control',1,'p_control','main.py',40),
  ('if -> tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLON','if',8,'p_if','main.py',43),
  ('ifelse -> tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE else','ifelse',8,'p_ifelse','main.py',46),
  ('else -> tk_else LBRACE codigo RBRACE SEMICOLON','else',5,'p_else','main.py',49),
  ('while -> tk_while LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLON','while',8,'p_while','main.py',52),
  ('funcion -> function tipo LPAREN argumento RPAREN SEMICOLON','funcion',6,'p_funcion','main.py',57),
  ('procedimiento -> procedure IDENT LPAREN argumento RPAREN SEMICOLON','procedimiento',6,'p_procedimiento','main.py',60),
  ('pin -> PIN LPAREN ENTERO SPACE conector RPAREN SEMICOLON','pin',7,'p_pin','main.py',63),
  ('conector -> IN','conector',1,'p_conector','main.py',66),
  ('conector -> OUT','conector',1,'p_conector','main.py',67),
  ('argumento -> argumento','argumento',1,'p_argumento','main.py',70),
  ('argumento -> LPAREN IDENT VAR_ASSING tipo RPAREN','argumento',5,'p_argumento','main.py',71),
  ('argumento -> empty','argumento',1,'p_argumento','main.py',72),
  ('libreria -> library LPAREN SINGLEDOT TEXTO PUNTO TEXTO SINGLEDOT RPAREN SEMICOLON','libreria',9,'p_libreria','main.py',77),
  ('loop -> adelante','loop',1,'p_loop','main.py',80),
  ('loop -> atras','loop',1,'p_loop','main.py',81),
  ('loop -> izquierda','loop',1,'p_loop','main.py',82),
  ('loop -> derecha','loop',1,'p_loop','main.py',83),
  ('loop -> esperar','loop',1,'p_loop','main.py',84),
  ('loop -> parar','loop',1,'p_loop','main.py',85),
  ('loop -> empty','loop',1,'p_loop','main.py',86),
  ('adelante -> foward LPAREN RPAREN SEMICOLON','adelante',4,'p_adelante','main.py',89),
  ('atras -> backward LPAREN RPAREN SEMICOLON','atras',4,'p_atras','main.py',92),
  ('izquierda -> left LPAREN RPAREN SEMICOLON','izquierda',4,'p_izquierda','main.py',95),
  ('derecha -> right LPAREN RPAREN SEMICOLON','derecha',4,'p_derecha','main.py',98),
  ('esperar -> wait LPAREN ENTERO RPAREN SEMICOLON','esperar',5,'p_esperar','main.py',101),
  ('parar -> stop LPAREN RPAREN SEMICOLON','parar',4,'p_parar','main.py',104),
  ('expression -> expression SUM term','expression',3,'p_expression_op','main.py',109),
  ('expression -> expression RESTA term','expression',3,'p_expression_op','main.py',110),
  ('expression -> term','expression',1,'p_expression_op','main.py',111),
  ('expression -> tipo','expression',1,'p_expression_op','main.py',112),
  ('expression -> variable','expression',1,'p_expression_op','main.py',113),
  ('term -> term PROD factor','term',3,'p_expression_op','main.py',114),
  ('term -> term DIV factor','term',3,'p_expression_op','main.py',115),
  ('term -> factor','term',1,'p_expression_op','main.py',116),
  ('factor -> ENTERO','factor',1,'p_factor','main.py',119),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','main.py',120),
  ('condicion -> expression relacion expression','condicion',3,'p_condicion','main.py',123),
  ('condicion -> NOT expression','condicion',2,'p_condicion','main.py',124),
  ('condicion -> expression logico expression','condicion',3,'p_condicion','main.py',125),
  ('relacion -> IGUAL','relacion',1,'p_relacion','main.py',128),
  ('relacion -> MAYOR','relacion',1,'p_relacion','main.py',129),
  ('relacion -> MENOR','relacion',1,'p_relacion','main.py',130),
  ('relacion -> MAYOR_IGUAL','relacion',1,'p_relacion','main.py',131),
  ('relacion -> MENOR_IGUAL','relacion',1,'p_relacion','main.py',132),
  ('logico -> and','logico',1,'p_logico','main.py',135),
  ('logico -> or','logico',1,'p_logico','main.py',136),
  ('empty -> <empty>','empty',0,'p_empty','main.py',140),
]