# Clase parser con los métodos y datos necesarios para hacer un análisis de sintaxis
class Parser:

    # Constructor
    def __init__(self, tokens, tokenCode):
        self.tokens = tokens
        self.tokenCode = tokenCode
        self.token = None


    # Módulo main
    def main(self):

        # Si ya no hay más entradas se considera épsilon y termina el programa
        if len(self.tokens) <= 0:
            print("Parser ejecutado con exito...")

        else:
            self.token = self.tokens.pop(0) # Obtener token actual
            self.line() # Ejecutar módulo line
            self.main() # Ejecutar módulo main


    # Módulo line
    def line(self):

        # Puede ser controlLine
        if self.token == self.tokenCode["controlLine"]:
            print("- Control Line")

        # Si no es checar si es dataLine
        else:
            self.dataLine()


    # Módulo dataLine
    def dataLine(self):

        # Puede ser dataLine y empezar con instrument
        if self.token == self.tokenCode["instrument"]:
            self.notes() # Ejecutar módulo notes
        
        # Si no es instrument y tampoco controlLine marcar error
        else:
            print("")
            print("ERROR: Sintaxis no valida, se esperaba controlLine o instrument")
            print("")
            quit()


    # Módulo notes
    def notes(self):

        self.token = self.tokens.pop(0) # Obtener token actual

        # Puede ser note
        if self.token == self.tokenCode["note"]:
            self.notes()

        # Puede ser bar
        elif self.token == self.tokenCode["bar"]:
            self.notes()

        # Puede ser newline
        elif self.token == self.tokenCode["newline"]:
            print("- Data Line")
            
        # Si es otro token hay un error de sintaxis
        else:
            print("")
            print("ERROR: Sintaxis no valida, se esperaba note, bar o newline")
            print("")
            quit()