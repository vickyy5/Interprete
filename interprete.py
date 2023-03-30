import scanner
import tipo_token
import tokeen
import sys

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

    def error(self,linea,mensaje):
        # Método para reportar un error encontrado durante la ejecución del código

        self.reportar(linea,"",mensaje)

    def reportar(self,linea,donde,mensaje):
        # Método para reportar información al usuario durante la ejecución del código

        print(f"[linea {linea}] Error {donde}: {mensaje}")
        pass


    def ejecutar(self,source):
        # Método para ejecutar el código ingresado

        self.scanner = scanner.Scanner(source)
        self.tokens = self.scanner.ScanTokens()

        for token in self.tokens:
            print(token)




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
    
    
