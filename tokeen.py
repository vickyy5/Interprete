from tipo_token import TipoToken

class Token:

    def __init__(self,tipo:TipoToken,lexema:str,literal,linea:int) -> None:
        self.tipo = tipo
        self.lexema = lexema
        self.literal = literal ##Palabra reservada no lleva literal
        self.linea = linea
    
    def __repr__(self) -> str:
        return f"<{self.tipo}, lexema:{self.lexema}, literal:{self.literal}, linea:{self.linea}>"
                 # <TipoToken.FUN: 'fun'>    

