import ply.yacc as yacc
# Get the token map from lexico.py
from lexico import tokens
from transpilador.transpilador import transpiler
from transpilador.code_generator import *

is_first_pin = False
is_first_reserved = False
# Body parser
def p_body(p):
    'beginend : begin codigo end'
    pass


def p_codigo(p):
    '''codigo : sentencia
              | sentencia codigo'''
    pass


def p_sentencia(p):
    '''sentencia : libreria sentencia
                 | variable sentencia
                 | control sentencia
                 | definicion sentencia
                 | procedimiento sentencia
                 | pin sentencia
                 | funcion sentencia
                 | loop sentencia
                 | empty'''
    pass

def p_var_tipo(p):
    '''var_tipo : INTEGER
                | STRING
                | FLOAT
                | BOOLEAN'''
    pass


def p_definicion(p):
    'definicion : var LPAREN IDENT VAR_ASSING INTEGER RPAREN SEMICOLON'
    transpiler(p, cg_variable)
    pass


def p_tipo(p):
    '''tipo : ENTERO
            | DECIMAL
            | LOGICO'''
    pass


def p_variable(p):
    '''variable : IDENT ASSING ENTERO SEMICOLON variable
                | IDENT ASSING ENTERO SEMICOLON'''
    transpiler(p, cg_asignacion)
    pass

# sintaxis para estructuras de control
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


# funciones y procedimientos
def p_funcion(p):
    'funcion : function var_tipo LPAREN argumento RPAREN SEMICOLON'
    pass


def p_procedimiento(p):
    'procedimiento : procedure IDENT LPAREN argumento RPAREN SEMICOLON'
    pass

def p_pin(p):
    'pin : PIN LPAREN IDENT VAR_ASSING PINTYPE RPAREN SEMICOLON'
    is_first_pin = True if p_pin.counter <= 0 else False
    p_pin.counter += 1
    transpiler(p, cg_pin, pin=is_first_pin, is_Pin=True)
    pass
p_pin.counter = 0

def p_argumento(p):
    '''argumento : argumento
                | LPAREN IDENT VAR_ASSING var_tipo RPAREN
                | empty'''
    pass


# Funciones establecidas y librerias
def p_libreria(p):
    '''libreria : library LPAREN SINGLEDOT IDENT PUNTO IDENT SINGLEDOT RPAREN SEMICOLON
                | empty'''
    transpiler(p, cg_libreria)
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
    is_first_reserved = True if p_adelante.counter <= 0 else False
    p_adelante.counter += 1
    transpiler(p, cg_avanzar, is_Reserved=is_first_reserved, reserved=True)
    pass
p_adelante.counter = 0


def p_atras(p):
    'atras : backward LPAREN RPAREN SEMICOLON'
    is_first_reserved = True if p_atras.counter <= 0 else False
    p_atras.counter += 1
    transpiler(p, cg_retroceder, is_Reserved=is_first_reserved, reserved=True)
    pass
p_atras.counter = 0


def p_izquierda(p):
    'izquierda : left LPAREN RPAREN SEMICOLON'
    is_first_reserved = True if p_izquierda.counter <= 0 else False
    p_izquierda.counter += 1
    transpiler(p, cg_izquierda, is_Reserved=is_first_reserved, reserved=True)
    pass
p_izquierda.counter = 0


def p_derecha(p):
    'derecha : right LPAREN RPAREN SEMICOLON'
    is_first_reserved = True if p_derecha.counter <= 0 else False
    p_derecha.counter += 1
    transpiler(p, cg_derecha, is_Reserved=is_first_reserved, reserved=True)
    pass
p_derecha.counter = 0


def p_esperar(p):
    'esperar : wait LPAREN ENTERO RPAREN SEMICOLON'
    is_first_reserved = True if p_esperar.counter <= 0 else False
    p_esperar.counter += 1
    transpiler(p, cg_esperar, is_Reserved=is_first_reserved, reserved=True)
    pass
p_esperar.counter = 0


def p_parar(p):
    'parar : stop LPAREN RPAREN SEMICOLON'
    is_first_reserved = True if p_parar.counter <= 0 else False
    p_parar.counter += 1
    transpiler(p, cg_parar, is_Reserved=is_first_reserved, reserved=True)
    pass
p_parar.counter = 0


# operaciones y condiciones
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
    print("Error sintáctico en la línea: " + str(p.lineno)
          + ". No se esperaba el token: " + str(p.value))


# Build the parser
parser = yacc.yacc(optimize=1)
try:
    with open("test.txt", "r") as file:
        data = file.read()
        file.close()
        try:
            parser.parse(data)
            print('Analisis sintáctico Correcto!')
        except:
            print('Analisis sintáctico Incorrecto!')
except IndexError:
    print("Error al leer el archivo")