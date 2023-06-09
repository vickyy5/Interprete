from tipo_token import TipoToken

class Token:
    # Clase para representar los tokens encontrados por el scanner

    def __init__(self,tipo:TipoToken,lexema:str,literal,linea:int) -> None:
        self.type = tipo
        self.lexeme = lexema
        self.literal = literal ##Palabra reservada no lleva literal
        self.line = linea

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return self.tipo == other.tipo
    
    def __repr__(self) -> str:
        return f"<{self.tipo}, lexema:{self.lexema}, literal:{self.literal}, linea:{self.linea}>"
        # <TipoToken.FUN: 'fun'>  
