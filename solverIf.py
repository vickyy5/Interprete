from nodo import Nodo
from tipo_token import TipoToken
import tablasimbolos as ts
from solverRel import SolverRel
#from arbol import Arbol
from tokeen import Token

class SolverIf:
    def __init__(self) -> None:
        pass

    def resolverIf(self, n:Nodo):
        if n.hijos is None:
            if n.value.type == TipoToken.NUMBER or n.value.type == TipoToken.STRING:
                return n.value.literal
            elif n.value.type == TipoToken.IDENTIFIER:
                return ts.simbolos.obtener(n.value.lexeme)
            
        cond = n.hijos[0]
        aux = SolverRel()
        rcond = aux.resolver(cond)
        print(f"******{rcond}")

        if n.hijos[-1].value.type == TipoToken.ELSE:
            el = True
            ebody = n.hijos[-1].hijos
        else:
            body = n.hijos[1:]
            el = False
        

        if rcond:
            raiz = Nodo(Token(TipoToken.NULL,"","",None))
            raiz.insertar_hijos(body)
            araux = Arbol(raiz) 
            araux.recorrer()
        else:
            if el:
                raiz = Nodo(Token(TipoToken.NULL,"","",None))
                raiz.insertar_hijos(ebody)
                araux = Arbol(raiz) 
                araux.recorrer()
            else:
                pass



            
        