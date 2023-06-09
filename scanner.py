import re
from tipo_token import TipoToken #Importar la clase TipoToken del módulo tipo_token
from tokeen import Token #Importar la clase Token del módulo token
import string  #Importar el módulo string

class Scanner: #Clase Scanner
    def __init__(self,source) -> None: #Definir el método constructor de la clase
        self.source = source
        self.__linea = 1  #Asignar el atributo linea a la instancia de la clase, con valor inicial de 1
        self.tokens = []  #Asignar el atributo tokens a la instancia de la clase, con una lista vacía como valor inicial
        self.palabras_reservadas = { # Diccionario con las palabras reservadas y su tipo de token correspondiente
            # "palabra" - "tipo token" 
            'and': TipoToken.AND,
            'class': TipoToken.CLASS,
            'also': TipoToken.ALSO,
            'for': TipoToken.FOR,
            'fun' : TipoToken.FUN,
            'if' : TipoToken.IF,
            'null' : TipoToken.NULL,
            'print' : TipoToken.PRINT,
            'return' : TipoToken.RETURN,
            'super' : TipoToken.SUPER,
            'this' : TipoToken.THIS,
            'true' : TipoToken.TRUE,
            'var' : TipoToken.VAR,
            'while' : TipoToken.WHILE,
        } 

    def ScanTokens(self): # -> list[TipoToken]:
        ##Aqui va el scanner


        self.estado = 0

        for line in self.source:
            current = ""
            line1 = self.clean(line)
            line1 +=" "
             # Ciclo for que recorre cada caracter en la línea ya limpia
            for char in line1:
                match self.estado: # Inicia un bloque de comparaciones de acuerdo al valor de la variable estado
                    case 0:
                        if char == "<": # Dependiento del caracter actual el en este caso es "<", se cambia el valor de estado a 1
                            self.estado = 1
                        elif char == "=":
                            self.estado = 2
                        elif char == ">":
                            self.estado = 3
                        elif char.isdigit(): # Si el caracter actual es un dígito, se agrega a la variable current y se cambia el valor de estado a 4
                           current += char
                           self.estado = 4
                        elif char.isalpha():
                            current += char
                            self.estado = 5
                        elif char == "/":
                            self.estado = 6
                        elif char == "{": # Si el caracter actual es "{", se agrega un token de tipo TipoToken.ALLAVE a la lista tokens, y se cambia el valor de estado a 0
                            self.tokens.append(Token(TipoToken.BRACKET_OPEN,"{",None,self.__linea))
                            self.estado = 0
                        elif char == "}":
                            self.tokens.append(Token(TipoToken.BRACKET_CLOSE,"}",None,self.__linea))
                            self.estado = 0
                        elif char == "(":
                            self.tokens.append(Token(TipoToken.PARENT_OPEN,"(",None,self.__linea))
                            self.estado = 0
                        elif char == ")":
                            self.tokens.append(Token(TipoToken.PARENT_CLOSE,")",None,self.__linea))
                            self.estado = 0
                        elif char == "+":
                            self.tokens.append(Token(TipoToken.SUB,"+",None,self.__linea))
                            self.estado = 0
                        elif char == "-":
                            self.tokens.append(Token(TipoToken.SUB,"-",None,self.__linea))
                            self.estado = 0
                        elif char == "*":
                            self.tokens.append(Token(TipoToken.MULT,"*",None,self.__linea))
                            self.estado = 0
                        elif char == "!":
                            self.estado = 8
                        elif char == '"':
                            current += char
                            self.estado = 9
                        elif char == ";":
                            self.tokens.append(Token(TipoToken.SEMICOLON,";",None,self.__linea))
                            self.estado = 0
                        elif char == ",":
                            self.tokens.append(Token(TipoToken.COMMA,",",None,self.__linea))
                            self.estado = 0
                        else:# Si el carácter actual no es ninguno de los anteriores: No hacemos nada y pasamos al siguiente carácter.
                            pass
                    case 1: # Si el estado actual es 1:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.LESS_EQUAL,"<=",None,self.__linea)) # Añadimos un nuevo objeto Token a la lista de tokens.
                            self.estado = 0 # Cambiamos el estado del scanner a 0.
                        else:
                            self.tokens.append(Token(TipoToken.LESS_THAN,"<",None,self.__linea))
                            self.estado = 0
                    case 2:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.EQUAL,"==",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.ASIGNATION,"=",None,self.__linea))
                            self.estado = 0
                    case 3:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.GREAT_EQUAL,">=",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.GREAT,">",None,self.__linea))
                            self.estado=0
                        pass
                    case 4:
                        if char.isdigit() or char == ".":
                            current += char
                        else:
                            self.tokens.append(Token(TipoToken.NUMBER,current,current,self.__linea))
                            current = ""
                            self.estado = 0
                    case 5:
                        if char.isdigit() or char.isalpha():
                            current += char
                        else:
                            if current in self.palabras_reservadas:
                                self.tokens.append(Token(self.palabras_reservadas[current],current,None,self.__linea))
                                current = ""
                                self.estado = 0
                            else:
                                self.tokens.append(Token(TipoToken.IDENTIFIER,current,None,self.__linea))
                                current = ""
                                self.estado = 0
                    case 6:
                        if char == "/":
                            self.estado = 7
                        elif char == "*":
                            self.estado = 11
                        else:
                            self.tokens.append(Token(TipoToken.DIAG,"/",None,self.__linea))
                            self.estado = 0
                    case 7:
                        if char == "\n":
                            self.estado = 0
                        else:
                            self.estado = 7
                    case 8:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.DIFERENT,"!=",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.NEGATION,"!",None,self.__linea))
                            self.estado = 0
                    case 9:
                        if char == '"':
                            current += char
                            self.tokens.append(Token(TipoToken.IDENTIFIER,current,current[1:-1],self.__linea))
                            current = ""
                            self.estado = 0
                        else:
                            current += char
                    case 11:
                        if char == "*":
                            self.estado = 12
                    case 12:
                        if char == "/":
                            self.estado = 0
                        else:
                            self.estado = 11

            self.__linea += 1 # Despues de leer la primera linea se incrementa
                        
        self.tokens.append(Token(TipoToken.EOF,None,None,self.__linea-1)) # Se termina el archivo y se agrega el token EOF
        return self.tokens # Devuelve la lista de tokens generada

    def clean(self,cadena): # Define una función 'clean' que toma una cadena como entrada y devuelve una cadena limpia
        simbolos = ['(', ')' ,'{' ,'}', '=', '<', '>', '!', '+', '-', ';', '*', '/']   # Define una lista de Símbolos
        clean_str = ''

        pattern = r'\/\/.*|\/\*[\s\S]*?\*\/|([A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|\S)'
        result = re.findall(pattern, cadena)    
        
        clean_str = " ".join(result)

        

        clean_str=clean_str.replace("/ *","/*")
        clean_str=clean_str.replace("* /","*/")
        clean_str=clean_str.replace("> =",">=")
        clean_str=clean_str.replace("< =","<=")
        clean_str=clean_str.replace("= =","==")

        #print(clean_str)

        return f"{clean_str}\n"

        
