import sys
from scanner import Scanner
from tokeen import Token
from tipo_token import TipoToken
from parser import Parser

class Interprete:
    # Clase principal del intérprete

    def __init__(self) -> None:
        self.existenErrores = False

                
    def ejecutarArchivo(self,archivo):
        # Método para ejecutar un archivo con código

        
        with open(archivo,'r') as file:
            lineas = file.readlines()

        #print(type(lineas))
        self.ejecutar(lineas)        

        if self.existenErrores:
            sys.exit()        

    def ejecutarPrompt(self):
        # Método para ejecutar el prompt del intérprete
        
        lineas=[]
        while True:
            try:
                linea = input("MiPromt>>> ")
                lineas.append(linea)
            except EOFError:
                break
            if not linea:
                continue 
            self.ejecutar(lineas)

    def error(linea,msj):
        # Método para reportar un error encontrado durante la ejecución del código
        print(f'[line {linea}] | {msj}')
        pass
        # self.report(self, msg, lin)


    def reportar(self,linea,donde,mensaje):
        # Método para reportar información al usuario durante la ejecución del código
        pass


    def ejecutar(self,source):
        # Método para ejecutar el código ingresado

        self.scanner = Scanner(source)
        self.tokens = self.scanner.ScanTokens()
        self.parser = Parser(self.tokens)
        self.parser.parse()



def main():
    # Función principal del intérprete
    interprete = Interprete()

    if len(sys.argv) > 2:
        print("Uso: interprete [script]")
        sys.exit()
    if len(sys.argv) == 2:
        interprete.ejecutarArchivo(sys.argv[1])
    else:
        interprete.ejecutarPrompt()


if __name__ == '__main__':
    main()    
    
    
