import scanner
import tipo_token
import tokeen
import sys

class Interprete:
    def __init__(self) -> None:
        self.existenErrores = False

                
    def ejecutarArchivo(self,archivo):
        
        with open(archivo,'r') as file:
            lineas = file.readlines()

        #print(type(lineas))
        self.ejecutar(lineas)        

        if self.existenErrores:
            sys.exit()        

    def ejecutarPrompt(self):
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

    def error(self,linea,mensaje):
        self.reportar(linea,"",mensaje)

    def reportar(self,linea,donde,mensaje):
        print(f"[linea {linea}] Error {donde}: {mensaje}")
        pass


    def ejecutar(self,source):
        self.scanner = scanner.Scanner(source)
        self.tokens = self.scanner.ScanTokens()

        for token in self.tokens:
            print(token)




def main():
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
    
    
