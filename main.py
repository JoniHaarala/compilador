import ply.yacc as yacc
import sys
# Get the token map from lexico.py
from lexico import tokens

# Body perser
def p_body(p):
    'beginend : begin codigo end'
    pass
def p_codigo(p):
    '''codigo : sentencia
              | sentencia codigo'''
    pass
def p_sentencia(p):
    '''sentencia : libreria
                 | variable
                 | control
                 | definicion
                 | procedimiento
                 | funcion
                 | loop'''
    pass
def p_definicion(p):
    'definicion : var LPAREN IDENT VAR_ASSING tipo RPAREN SEMICOLON'
    pass
def p_variable(p):
    'variable : IDENT ASSING tipo SEMICOLON'
    pass
def p_tipo(p):
    '''tipo : TEXTO
            | ENTERO
            | DECIMAL
            | LOGICO'''
    pass

#sintaxis para estructuras de control
def p_control(p):
    '''control : if
               | ifelse
               | while'''
    pass
def p_if(p):
    'if : tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLON'
    pass
def p_ifelse(p):
    'ifelse : tk_if LPAREN condicion RPAREN LBRACE codigo RBRACE else'
    pass
def p_else(p):
    'else : tk_else LBRACE codigo RBRACE SEMICOLON'
    pass
def p_while(p):
    'while : tk_while LPAREN condicion RPAREN LBRACE codigo RBRACE SEMICOLON'
    pass

#funciones y procedimientos
def p_funcion(p):
    'funcion : function tipo LPAREN argumento RPAREN SEMICOLON'
    pass
def p_procedimiento(p):
    'procedimiento : procedure IDENT LPAREN argumento RPAREN SEMICOLON'
    pass
def p_pin(p):
    'pin : PIN LPAREN ENTERO SPACE conector RPAREN SEMICOLON'
    pass
def p_conector(p):
    '''conector : IN
                | OUT'''
    pass
def p_argumento(p):
    '''argumento : argumento
                | LPAREN IDENT VAR_ASSING tipo RPAREN
                | empty'''
    pass

# Funciones establecidas y librerias
def p_libreria(p):
    'libreria : library LPAREN SINGLEDOT TEXTO PUNTO TEXTO SINGLEDOT RPAREN SEMICOLON'
    pass
def p_loop(p):
    '''loop : adelante
            | atras
            | izquierda
            | derecha
            | esperar
            | parar
            | empty'''
    pass
def p_adelante(p):
    'adelante : foward LPAREN RPAREN SEMICOLON'
    pass
def p_atras(p):
    'atras : backward LPAREN RPAREN SEMICOLON'
    pass
def p_izquierda(p):
    'izquierda : left LPAREN RPAREN SEMICOLON'
    pass
def p_derecha(p):
    'derecha : right LPAREN RPAREN SEMICOLON'
    pass
def p_esperar(p):
    'esperar : wait LPAREN ENTERO RPAREN SEMICOLON'
    pass
def p_parar(p):
    'parar : stop LPAREN RPAREN SEMICOLON'
    pass

#operaciones y condiciones
def p_expression_op(p):
    '''expression : expression SUM term
                  | expression RESTA term
                  | term
                  | tipo
                  | variable
       term       : term PROD factor
                  | term DIV factor
                  | factor'''
    pass
def p_factor(p):
    '''factor : ENTERO
              | LPAREN expression RPAREN'''
    pass
def p_condicion(p):
    '''condicion : expression relacion expression
                 | NOT expression
                 | expression logico expression'''
    pass
def p_relacion(p):
    '''relacion : IGUAL
                | MAYOR
                | MENOR
                | MAYOR_IGUAL
                | MENOR_IGUAL'''
    pass
def p_logico(p):
    '''logico : and
              | or'''
    pass

def p_empty(p):
    'empty :'
    pass
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc(optimize=1)

try:
    f = open('test.txt')
    data = f.read()
    f.close()
except IndexError:
    sys.stdout.write('Reading from standard input (type EOF to end):\n')
    data = sys.stdin.read()

try:
    parser.parse(data)
    print('Analisis sintáctico Correcto!')
except:
    print('Analisis sintáctico Incorrecto!')
