from tipo_token import TipoToken
from tokeen import Token
import string 

class Scanner:
    def __init__(self,source) -> None:
        self.source = source
        self.__linea = 1
        self.tokens = []
        ##lista de tokens
        self.palabras_reservadas = {
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

        print(self.source)        

        estado = 0

        for line in self.source:
            current = ""
            line1 = self.clean(line)
            line1 +=" "
            #print(f"{line1}")
            for char in line1:
                #print(f"{estado} -> {char}")
                match estado:
                    case 0:
                        if char == "<":
                            estado = 1
                        elif char == "=":
                            estado = 2
                        elif char == ">":
                            estado = 3
                        elif char.isdigit():
                           current += char
                           estado = 4
                        elif char.isalpha():
                            current += char
                            estado = 5
                        elif char == "/":
                            estado = 6
                        elif char == "{":
                            self.tokens.append(Token(TipoToken.ALLAVE,"{",None,self.__linea))
                            estado = 0
                        elif char == "}":
                            self.tokens.append(Token(TipoToken.CLLAVE,"}",None,self.__linea))
                            estado = 0
                        elif char == "(":
                            self.tokens.append(Token(TipoToken.APARE,"(",None,self.__linea))
                            estado = 0
                        elif char == ")":
                            self.tokens.append(Token(TipoToken.CPARE,")",None,self.__linea))
                            estado = 0
                        elif char == "+":
                            self.tokens.append(Token(TipoToken.MAS,"+",None,self.__linea))
                            estado = 0
                        elif char == "-":
                            self.tokens.append(Token(TipoToken.MENOR,"-",None,self.__linea))
                            estado = 0
                        elif char == "*":
                            self.tokens.append(Token(TipoToken.POR,"*",None,self.__linea))
                            estado = 0
                        elif char == "!":
                            estado = 8
                        elif char == '"':
                            current += char
                            estado = 9
                        elif char == ";":
                            self.tokens.append(Token(TipoToken.PYCOMA,";",None,self.__linea))
                            estado = 0
                        elif char == ",":
                            self.tokens.append(Token(TipoToken.COMA,",",None,self.__linea))
                            estado = 0
                        else:
                            pass
                    case 1:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MENORIGUAL,"<=",None,self.__linea))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.MENOR,"<",None,self.__linea))
                            estado = 0
                    case 2:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.IGUALQUE,"==",None,self.__linea))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.ASIGNACION,"=",None,self.__linea))
                            estado = 0
                    case 3:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MAYORIGUAL,">=",None,self.__linea))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.MAYOR,">",None,self.__linea))
                            estado=0
                        pass
                    case 4:
                        if char.isdigit() or char == ".":
                            current += char
                        else:
                            self.tokens.append(Token(TipoToken.NUMERO,current,current,self.__linea))
                            current = ""
                            estado = 0
                    case 5:
                        if char.isdigit() or char.isalpha():
                            current += char
                        else:
                            if current in self.palabras_reservadas:
                                self.tokens.append(Token(self.palabras_reservadas[current],current,None,self.__linea))
                                current = ""
                                estado = 0
                            else:
                                self.tokens.append(Token(TipoToken.IDENTIFICADOR,current,None,self.__linea))
                                current = ""
                                estado = 0
                    case 6:
                        if char == "/":
                            estado = 7
                        elif char == "*":
                            estado = 11
                        else:
                            self.tokens.append(Token(TipoToken.ENTRE,"/",None,self.__linea))
                            estado = 0
                    case 7:
                        if char == "\n":
                            estado = 0
                        else:
                            estado = 7
                    case 8:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.DIFF,"!=",None,self.__linea))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.NEGA,"!",None,self.__linea))
                            estado = 0
                    case 9:
                        if char == '"':
                            current += char
                            self.tokens.append(Token(TipoToken.IDENTIFICADOR,current,current[1:-1],self.__linea))
                            current = ""
                            estado = 0
                        else:
                            current += char
                            #estado = 9
                    case 11:
                        if char == "*":
                            estado = 12
                    case 12:
                        if char == "/":
                            estado = 0
                        else:
                            estado = 11

            self.__linea += 1
                        
        self.tokens.append(Token(TipoToken.EOF,None,None,self.__linea-1))
        return self.tokens

    def clean(self,cadena):
        simbolos = ['(', ')' ,'{' ,'}', '=', '<', '>', '!', '+', '-', ';', '*', '/']
        clean_str = ''
        current = ''
        control = True
        estado = 0
        char = 0
        cadena = cadena.replace(" ","")
        #print(f"*{cadena}*")
        while control:
            match estado:
                case 0:
                    try:
                        if cadena[char] in simbolos:
                            current = cadena[char]
                            estado = 1
                        elif cadena[char].isdigit():
                            current = cadena[char]
                            estado = 2
                        elif cadena[char].isalpha():
                            current += cadena[char]
                            estado = 3
                        elif cadena[char] == '"':
                            current += cadena[char]
                            estado = 4
                        else:
                            control = False
                    except:
                        control = False
                case 1:
                    try:
                        if cadena[char+1] in simbolos:
                            current += cadena[char+1]
                            char +=1
                            estado = 1
                        else:
                            clean_str += f" {current}"
                            current = ""
                            char += 1
                            estado = 0
                    except:
                        clean_str += f" {current} "
                        current = ""
                        char += 1
                        estado = 0
                        control = False

                case 2:
                    try:
                        if cadena[char+1].isdigit() or cadena[char+1] == ".":
                            #print(cadena[char+1])
                            current += cadena[char+1]
                            char +=1
                        elif cadena[char+1] == ",":
                            clean_str += f" {current} ,"
                            char += 2
                            current = ""
                            estado = 0
                        else:
                            #print(cadena[char+1])
                            clean_str += f" {current}"
                            current = ""
                            char += 1
                            estado = 0
                    except:
                        clean_str += f" {current}"
                        current = ""
                        char += 1
                        estado = 0
                        control = False
                case 3:
                    try:
                        if cadena[char+1].isalpha() or cadena[char+1].isdigit():
                            current += cadena[char+1]
                            char += 1
                        elif cadena[char+1] == ",":
                            clean_str += f" {current} ,"
                            char += 2
                            current = ""
                            estado = 0
                        else:
                            clean_str += f" {current} "
                            current = ""
                            char += 1
                            estado = 0
                    except:
                        control = False
                case 4:
                    try:
                        if cadena[char+1] != '"':
                            current += cadena[char+1]
                            char +=1
                        else:
                            clean_str += f' {current}" '
                            current = ""
                            char +=1
                            estado = 0
                    except:
                        control = False
            
        return f"{clean_str}\n"





        
