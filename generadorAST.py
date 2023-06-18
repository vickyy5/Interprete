from tipo_token import TipoToken
from tokeen import Token


class GeneradorAST:
    def __init__(self, postfija:list[Token]) -> None:
        self.postfija = postfija
        self.stack = []

    