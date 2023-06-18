from tipo_token import TipoToken
from tokeen import Token
from nodo import Nodo

class Arbol:
    def __init__(self, raiz: Nodo) -> None:
        self.raiz = raiz
        
    def recorrer(self):
        
        for index,n in enumerate(self.raiz.hijos):
            t = n.value
            match t.type:
                case TipoToken.ADD, TipoToken.SUB, TipoToken.MULT, TipoToken.DIAG:
                    pass
                case TipoToken.VAR:
                    # Crear Variable, usar tabla de simbolos
                    pass
                case TipoToken.IF:
                    pass
            pass

        