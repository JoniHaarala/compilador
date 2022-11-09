def cg_libreria(p):
    codigo = list(p)
    result = "".join(["#include "] + ["<"] + codigo[4:5] + ["."] + codigo[6:7] + [">"] + ["\n"])
    return result


def cg_variable(p):
    codigo = list(p)
    if codigo[5] == "entero":
        result = "".join(['int'] + [" "] + [codigo[3]] + [";"] + ["\n"])
    elif codigo[5] == "decimal":
        result = "".join(['float'] + [" "] + [codigo[3]] + [";"] + ["\n"])
    elif codigo[5] == "string":
        result = "".join(['string'] + [" "] + [codigo[3]] + [";"] + ["\n"])
    else:
        result = "".join(['bool'] + [" "] + [codigo[3]] + [";"] + ["\n"])
    return result


def cg_asignacion(p):
    codigo = list(p)
    result = "".join([codigo[1]] + [" = "] + [str(codigo[3])] + [";"] + ["\n"])
    return result


def cg_condicional(p):
    codigo = list(p)
    result = "".join(["if ("] + [") "] + ["{"] + ["\n"] + ["}"] + ["\n"])
    return result


def cg_procendimiento(p):
    codigo = list(p)
    result = "".join([codigo[6]] + [" "] + [codigo[1]] + ["()"] + ["{"] + ["\n"] + ["}"] + ["\n"])
    return result


def cg_funcion(p):
    codigo = list(p)
    result = "".join([codigo[5]] + [codigo[2]] + ["()"] + ["{"] + ["\n"] + ["}"] + ["\n"])
    return result


def cg_comparacion(p):
    codigo = list(p)
    result = "".join([codigo[5]] + [" "] + [codigo[3]] + ["("] + [codigo[7]] + [");"] + ["\n"])
    return result


def cg_pin(p):
    codigo = list(p)
    if codigo[5] == "IN":
        result = "".join(["    pinMode("] + [codigo[3]] + [", "] + ["INPUT);"] + ["\n"])
    else:
        result = "".join(["    pinMode("] + [codigo[3]] + [", "] + ["OUTPUT);"] + ["\n"])
    return result


def cg_avanzar(p):
    codigo = list(p)
    return "".join(['    avanzar'] + [codigo[2]] + [codigo[3]] + [";"] + ["\n"])
def cg_retroceder(p):
    codigo = list(p)
    return "".join(['    parar'] + [codigo[2]] + [codigo[3]] + [";"] + ["\n"])
def cg_izquierda(p):
    codigo = list(p)
    return "".join(['    giro_izquierda'] + [codigo[2]] + [codigo[3]] + [";"] + ["\n"])
def cg_derecha(p):
    codigo = list(p)
    return "".join(['    giro_derecha'] + [codigo[2]] + [codigo[3]] + [";"] + ["\n"])
def cg_esperar(p):
    codigo = list(p)
    return "".join(['    delay'] + [codigo[2]] + [codigo[3]] + [codigo[4]] + [";"] + ["\n"])
def cg_parar(p):
    codigo = list(p)
    return "".join(['    parar'] + [codigo[2]] + [codigo[3]] + [";"] + ["\n"])

