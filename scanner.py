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

        for index,line in enumerate(self.source):
            current = ""
            #while control:
            for char in line:
                print(f"{estado} -> {char}")
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
                        else:
                            pass
                    case 1:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MENORIGUAL,"<=",None,index))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.MENOR,"<",None,index))
                            estado = 0
                    case 2:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.IGUALQUE,"==",None,index))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.ASIGNACION,"=",None,index))
                            estado = 0
                    case 3:
                        if char == "=":
                            self.tokens.append(Token(TipoToken.MAYORIGUAL,">=",None,index))
                            estado = 0
                        else:
                            self.tokens.append(Token(TipoToken.MAYOR,">",None,index))
                            estado=0
                        pass
                    case 4:
                        if char.isdigit():
                            current += char
                        elif char == ".":
                            current += char
                        else:
                            self.tokens.append(Token(TipoToken.NUMERO,current,current,index))
                            current = ""
                            estado = 0
                    case 5:
                        if char.isdigit() or char.isalpha():
                            current += char
                        else:
                            if current in self.palabras_reservadas:
                                self.tokens.append(Token(self.palabras_reservadas[current],current,None,index))
                                current = ""
                                estado = 0
                            else:
                                self.tokens.append(Token(TipoToken.IDENTIFICADOR,current,None,index))
                                current = ""
                                estado = 0
                        
                        
        self.tokens.append(Token(TipoToken.EOF,None,None,None))
        return self.tokens
                     

        #tokens.add(token) 
        #return token
        pass

    def automata(self):
        pass 


        