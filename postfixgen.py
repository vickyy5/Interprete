from tokeen import Token
from tipo_token import TipoToken


class Postfix:
    def __init__(self, tokens) -> None:
        self.infija = tokens
        self.stackk = []
        self.postfija = []
        self.palabras_reservadas = {  # Diccionario con las palabras reservadas y su tipo de token correspondiente
            # "palabra" - "tipo token"
            "and": TipoToken.AND,
            "class": TipoToken.CLASS,
            "also": TipoToken.ALSO,
            "for": TipoToken.FOR,
            "fun": TipoToken.FUN,
            "if": TipoToken.IF,
            "null": TipoToken.NULL,
            "print": TipoToken.PRINT,
            "return": TipoToken.RETURN,
            "super": TipoToken.SUPER,
            "this": TipoToken.THIS,
            "true": TipoToken.TRUE,
            "var": TipoToken.VAR,
            "while": TipoToken.WHILE,
            "else": TipoToken.ELSE
        }

    def convertir(self):
        estructuraDeControl = False
        stack_Estruc = []
        for index,t in enumerate(self.infija):
            if t.type == TipoToken.EOF:
                break
            
            if t.type in self.palabras_reservadas.values():
                self.postfija.append(t)
                if self.esEstructuraDeControl(t.type):
                    estructuraDeControl = True
                    stack_Estruc.append(t)
            elif self.esOperando(t.type):
                self.postfija.append(t)
            elif t.type == TipoToken.PARENT_OPEN:
                self.stackk.append(t)
            elif t.type == TipoToken.PARENT_CLOSE:
                #print(f"{estructuraDeControl} y {self.stackk[-1].type}")
                while( ( len(self.stackk) != 0) and (self.stackk[-1].type != TipoToken.PARENT_OPEN) ):
                    temp = self.stackk.pop()
                    #print(f"{temp}")
                    self.postfija.append(temp)
                if self.stackk[-1].type == TipoToken.PARENT_OPEN:
                    self.stackk.pop()
                if estructuraDeControl:
                    #print("semiak")
                    self.postfija.append(Token(TipoToken.SEMICOLON,";",";",None))
            elif self.esOperador(t.type):
                #print(f"si -> {t.type}")
                while len(self.stackk)!=0 and self.precedenciaMayorIgual(self.stackk[-1].type, t.type):
                    temp = self.stackk.pop()
                    self.postfija.append(temp)
                self.stackk.append(t)
            elif t.type == TipoToken.SEMICOLON:
                while len(self.stackk) !=0 and self.stackk[-1].type != TipoToken.BRACKET_OPEN:
                    temp = self.stackk.pop()
                    self.postfija.append(temp)
                self.postfija.append(t) 
            elif t.type == TipoToken.BRACKET_OPEN:
                self.stackk.append(t)
            elif t.type == TipoToken.BRACKET_CLOSE and estructuraDeControl:
                #print(f"caso else -> {self.infija[index+1].type}")
                if self.infija[index+1].type == TipoToken.ELSE:
                    self.stackk.pop()
                else:
                    self.stackk.pop()
                    #print("aki")
                    self.postfija.append(Token(TipoToken.SEMICOLON,";",";",None))
                    #self.postfija.append("semi")
                    stack_Estruc.pop()
                    if len(stack_Estruc) == 0:
                        estructuraDeControl = False

        while(len(self.stackk) != 0):
            temp = self.stackk.pop()
            self.postfija.append(temp)

        while( len(stack_Estruc) != 0):
            #print("sem")
            stack_Estruc.pop()
            self.postfija.append(Token(TipoToken.SEMICOLON,";",";",None))


        return self.postfija 

    def esOperando(self,tipo):
        match tipo:
            case TipoToken.IDENTIFIER:
                return True
            case TipoToken.NUMBER:
                return True
            case other:
                return False

    def esEstructuraDeControl(self,tipo):
        match tipo:
            case TipoToken.IF:
                return True
            case TipoToken.ELSE:
                return True
            case TipoToken.WHILE:
                return True
            case other:
                return False

    def esOperador(self,tipo):
        #print("esop")
        match tipo:
            case TipoToken.ADD:
                return True
            case TipoToken.SUB:
                return True
            case TipoToken.MULT:
                return True
            case TipoToken.DIAG:
                return True
            case TipoToken.EQUAL:
                return True
            case TipoToken.GREAT:
                return True
            case TipoToken.GREAT_EQUAL:
                return True
            case TipoToken.ASIGNATION:
                return True
            case TipoToken.LESS_THAN:
                return True
            case TipoToken.LESS_EQUAL:
                return True
            case other:
                return False


    def precedenciaMayorIgual(self, tipo1, tipo2):
        #print(f"{tipo1}->{self.obtenerPrecedencia(tipo1)} y  {tipo2}->{self.obtenerPrecedencia(tipo2)}")
        return  self.obtenerPrecedencia(tipo1) >= self.obtenerPrecedencia(tipo2)

    def obtenerPrecedencia(self,tipo):
        match tipo:
            case TipoToken.MULT:
                return 3 
            case TipoToken.DIAG:
                return 3
            case TipoToken.ADD:
                return 2
            case TipoToken.SUB:
                return 2
            case TipoToken.ASIGNATION:
                return 1
            case TipoToken.GREAT:
                return 1
            case TipoToken.GREAT_EQUAL:
                return 1
            case other:
                return 0


    
