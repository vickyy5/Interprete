from enum import Enum

class TipoToken(Enum):
    Y ="y"
    CLASE = "clase"
    ADEMAS = "ademas"
    FALSO = "falso"
    PARA = "para"
    FUN = "fun"
    SI = "si"
    NULO = "nulo"
    O = "o"
    IMPRIMIR = "imprimir"
    RETORNAR = "retornar"
    SUPER = "super"
    ESTE = "este"
    VERDADERO = "verdadero"
    VAR = "var"
    MIENTRAS = "mientras"
    EOF = "EOF"
    #Signos o símbolos del lenguaje:
    APARE = "("
    CPARE = ")"
    ALLAVE = "{"
    CLLAVE = "}"
    COMA = ","
    PUNTO = "."
    PYCOMA = ";"
    MENOS = "-"
    MAS = "+"
    POR = "*"
    ENTRE = "/"
    NEGA = "!"
    DIFF = "!="
    ASIGNACION = "="
    IGUALQUE = "=="
    MENOR = "<"
    MENORIGUAL = "<="
    MAYOR = ">"
    MAYORIGUAL = ">="
    COMENTARIO = "//" # -> comentarios (no se genera token)
    MULTICOMEN = "/* ... * /"  #-> comentarios (no se genera token)
    NUMERO = "NUM"
    IDENTIFICADOR = "ID"
    #Identificador,
    #Cadena
    #Numero
    #Cada palabra reservada tiene su nombre de token

