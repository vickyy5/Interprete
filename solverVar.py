from tipo_token import TipoToken
from tokeen import Token
import tablasimbolos as ts
from nodo import Nodo
import sys

class SolverVar:
    def __init__(self, nodo:Nodo) -> None:
        self.nodo:Nodo = nodo


    def solver(self):

        if len(self.nodo.hijos) == 2:
            key, value = "",0
            for i in self.nodo.hijos:
                if i.value.type == TipoToken.IDENTIFIER:
                    key = i.value.lexeme
                if ts.simbolos.existeIdentificador(key):
                    print(f"Error: La variable {key} ya estaba definida")
                    sys.exit()
                elif ( i.value.type == TipoToken.NUMBER ) or ( i.value.type == TipoToken.STRING ) or (i.value.type == TipoToken.TRUE) or (i.value.type == TipoToken.FALSE):
                    value = i.value.literal
            ts.simbolos.asignar(key,value)
            return
        elif len(self.nodo.hijos) == 1:
            if self.nodo.hijos[0].value.type == TipoToken.IDENTIFIER:
                key = self.nodo.hijos[0].value.lexeme
                if ts.simbolos.obtener(key):
                    print(f"Error: La variable {key} ya estaba definida")
                    sys.exit()
                ts.simbolos.asignar(key,None)
                return
        else:
            print("Error al declarar la variable")
            sys.exit()
        
        