import ply.lex as lex

reserved = {
    'BEGIN': 'begin',
    'END': 'end',
    'VAR': 'var',
    'and': 'and',
    'or': 'or',
    'IF': 'tk_if',
    'ELSE': 'tk_else',
    'WHILE': 'tk_while',
    'DEFF': 'function',
    'DEFP': 'procedure',
    'FOWARD': 'foward',
    'BACKWARD': 'backward',
    'LEFT': 'left',
    'RIGHT': 'right',
    'STOP': 'stop',
    'WAIT': 'wait',
    'in': 'library',
    'PIN': 'PIN',
    'IN': 'IN',
    'OUT': 'OUT'
}

tokens = [
             'IDENT',
             'TEXTO',
             'ENTERO',
             'DECIMAL',
             'LOGICO',
             'SUM',
             'RESTA',
             'PROD',
             'DIV',
             'IGUAL',
             'MAYOR',
             'MENOR',
             'MAYOR_IGUAL',
             'MENOR_IGUAL',
             'SEMICOLON',
             'VAR_ASSING',
             'ASSING',
             'LPAREN',
             'RPAREN',
             'LBRACE',
             'RBRACE',
             'LBRACKET',
             'RBRACKET',
             'COMMA',
             'SINGLEDOT',
             'DOUBLEDOT',
             'PUNTO',
             'NOT',
             'SPACE',
             'COMMENT'
         ] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUM = r'\+'
t_RESTA = r'\-'
t_PROD = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\=='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYOR_IGUAL = r'\>='
t_MENOR_IGUAL = r'\<='
t_SEMICOLON = r'\;'
t_VAR_ASSING = r'\:'
t_ASSING = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_SINGLEDOT = r'\''
t_DOUBLEDOT = r'\"'
t_PUNTO = r'\.'
t_NOT = r'\!'
t_ignore_SPACE = r'\t'


# A regular expression rule with some action code
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')  # Check for reserved words
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_DECIMAL(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t


def t_TEXTO(t):
    r'\w+'
    t.value = str(t.value)
    return t


def t_LOGICO(t):
    r'true|false'
    t.value = bool(t.value)
    return t


# Comment discard section
def t_COMMENT(t):
    r'\#.*'
    pass


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(imput, token):
    line_start = imput.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    print("Error in line "+str(t.lineno)+". Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(optimize=1)

f = open('test.txt')
data = f.read()
f.close()

#Give the lexer some input
lexer.input(data)

#Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
