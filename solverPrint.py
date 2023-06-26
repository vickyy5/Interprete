from tipo_token import TipoToken
from nodo import Nodo
import tablasimbolos as ts


class SolverPrint:
    def __init__(self) -> None:
        pass

    def resolver(self,n:Nodo):
        
        if n.hijos is None:
            if n.value.type == TipoToken.NUMBER or n.value.type == TipoToken.STRING:
                return n.value.literal
            elif n.value.type == TipoToken.IDENTIFIER:
                return ts.simbolos.obtener(n.value.lexeme)


        Hijo:Nodo = n.hijos[0]
        valor = self.resolver(Hijo)

        return valor


