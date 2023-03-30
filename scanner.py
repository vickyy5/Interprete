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
            "y" : TipoToken.Y,
            "clase" : TipoToken.CLASE,
            "ademas" : TipoToken.ADEMAS,
            "falso" : TipoToken.FALSO,
            "para" : TipoToken.PARA,
            "fun" : TipoToken.FUN,
            "si" : TipoToken.SI,
            "nulo" : TipoToken.NULO,
            "imprimir" : TipoToken.IMPRIMIR,
            "retornar" : TipoToken.RETORNAR,
            "super" : TipoToken.SUPER,
            "este" : TipoToken.ESTE,
            "verdadero" : TipoToken.VERDADERO,
            "var" : TipoToken.VAR,
            "mientras" : TipoToken.MIENTRAS
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
                            self.tokens.append(Token(TipoToken.ALLAVE,"{",None,self.__linea))
                            self.estado = 0
                        elif char == "}":
                            self.tokens.append(Token(TipoToken.CLLAVE,"}",None,self.__linea))
                            self.estado = 0
                        elif char == "(":
                            self.tokens.append(Token(TipoToken.APARE,"(",None,self.__linea))
                            self.estado = 0
                        elif char == ")":
                            self.tokens.append(Token(TipoToken.CPARE,")",None,self.__linea))
                            self.estado = 0
                        elif char == "+":
                            self.tokens.append(Token(TipoToken.MAS,"+",None,self.__linea))
                            self.estado = 0
                        elif char == "-":
                            self.tokens.append(Token(TipoToken.MENOR,"-",None,self.__linea))
                            self.estado = 0
                        elif char == "*":
                            self.tokens.append(Token(TipoToken.POR,"*",None,self.__linea))
                            self.estado = 0
                        elif char == "!":
                            self.estado = 8
                        elif char == '"':
                            current += char
                            self.estado = 9
                        elif char == ";":
                            self.tokens.append(Token(TipoToken.PYCOMA,";",None,self.__linea))
                            self.estado = 0
                        elif char == ",":
                            self.tokens.append(Token(TipoToken.COMA,",",None,self.__linea))
                            self.estado = 0
                        else:# Si el carácter actual no es ninguno de los anteriores: No hacemos nada y pasamos al siguiente carácter.
                            pass
                    case 1: # Si el estado actual es 1:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MENORIGUAL,"<=",None,self.__linea)) # Añadimos un nuevo objeto Token a la lista de tokens.
                            self.estado = 0 # Cambiamos el estado del scanner a 0.
                        else:
                            self.tokens.append(Token(TipoToken.MENOR,"<",None,self.__linea))
                            self.estado = 0
                    case 2:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.IGUALQUE,"==",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.ASIGNACION,"=",None,self.__linea))
                            self.estado = 0
                    case 3:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MAYORIGUAL,">=",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.MAYOR,">",None,self.__linea))
                            self.estado=0
                        pass
                    case 4:
                        if char.isdigit() or char == ".":
                            current += char
                        else:
                            self.tokens.append(Token(TipoToken.NUMERO,current,current,self.__linea))
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
                                self.tokens.append(Token(TipoToken.IDENTIFICADOR,current,None,self.__linea))
                                current = ""
                                self.estado = 0
                    case 6:
                        if char == "/":
                            self.estado = 7
                        elif char == "*":
                            self.estado = 11
                        else:
                            self.tokens.append(Token(TipoToken.ENTRE,"/",None,self.__linea))
                            self.estado = 0
                    case 7:
                        if char == "\n":
                            self.estado = 0
                        else:
                            self.estado = 7
                    case 8:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.DIFF,"!=",None,self.__linea))
                            self.estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.NEGA,"!",None,self.__linea))
                            self.estado = 0
                    case 9:
                        if char == '"':
                            current += char
                            self.tokens.append(Token(TipoToken.IDENTIFICADOR,current,current[1:-1],self.__linea))
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
        current = ''
        control = True
        self.estado = 0
        char = 0
        cadena = cadena.replace(" ","") # Reemplaza los espacios en blanco por nada
        while control: #Mientras que 'control' sea verdadero
            match self.estado: #Define un bloque 'match' que depende del estado actual
                case 0:
                    try:
                        if cadena[char] in simbolos: #Si el carácter actual está en la lista de símbolos
                            current = cadena[char] #establece la cadena actual al carácter actual
                            self.estado = 1 #establece el estado a 1
                        elif cadena[char].isdigit():
                            current = cadena[char]
                            self.estado = 2
                        elif cadena[char].isalpha():
                            current += cadena[char]
                            self.estado = 3
                        elif cadena[char] == '"':
                            current += cadena[char]
                            self.estado = 4
                        else:
                            control = False # Si no es ni símbolo, dígito ni letra, se acaba el bucle
                    except:
                        control = False
                case 1:# Estado 1: se ha encontrado un símbolo
                    try:
                        # Si el siguiente caracter de 'cadena' también es un símbolo, se agrega al símbolo actual
                        if cadena[char+1] in simbolos:
                            current += cadena[char+1]
                            char +=1
                            self.estado = 1
                        else:
                            clean_str += f" {current}" # Si no hay más símbolos adyacentes, se agrega el símbolo actual a 'clean_str'
                            current = "" # Se reinicia la cadena temporal
                            char += 1 # Se incrementa el índice de 'cadena'
                            self.estado = 0 # Se regresa al estado 0 para procesar el siguiente caracter
                    except:
                        clean_str += f" {current} " # Si se llega al final de 'cadena', se agrega el símbolo actual a 'clean_str'
                        current = ""
                        char += 1
                        self.estado = 0
                        control = False
                # Estado 2: se ha encontrado un dígito
                case 2:
                    try:
                        if cadena[char+1].isdigit() or cadena[char+1] == ".": # Si el siguiente caracter es un dígito o un punto
                            current += cadena[char+1] # Se agrega el caracter actual a la cadena current
                            char +=1 # Se agrega el caracter actual a la cadena current
                        elif cadena[char+1] == ",": # Se agrega el caracter actual a la cadena current
                            clean_str += f" {current} ,"  # Se agrega el caracter actual a la cadena current
                            char += 2 # Se agrega el caracter actual a la cadena current
                            current = "" # Se agrega el caracter actual a la cadena current
                            self.estado = 0 # Se reinicia el valor del atributo "estado" a 0
                        else:
                            clean_str += f" {current}"
                            current = ""
                            char += 1
                            self.estado = 0
                    except:
                        clean_str += f" {current}"
                        current = ""
                        char += 1
                        self.estado = 0
                        control = False
                        # Estado 3: se ha encontrado una letra
                case 3:
                    try:
                        if cadena[char+1].isalpha() or cadena[char+1].isdigit():  # Si el siguiente caracter es una letra o un dígito
                            current += cadena[char+1] # Se agrega el caracter actual a la cadena current
                            char += 1  # Se aumenta el índice del caracter actual en 1
                        elif cadena[char+1] == ",": # Si el siguiente caracter es una ,
                            clean_str += f" {current} ,"
                            char += 2
                            current = ""
                            self.estado = 0
                        else:
                            clean_str += f" {current} "
                            current = ""
                            char += 1
                            self.estado = 0
                    except:
                        control = False
                case 4: # Estado 3: se ha encontrado un "
                    try: 
                        if cadena[char+1] != '"': # Si el siguiente caracter es diferente de un "
                            current += cadena[char+1] # seguir avanzando
                            char +=1
                        else:
                            clean_str += f' {current}" '
                            current = ""
                            char +=1
                            self.estado = 0
                    except:
                        control = False
            
        return f"{clean_str}\n"

        
