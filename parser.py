# Ejecutar parser para verificar sintaxis
def parser(tokens, tokenCode):

    # Módulo main
    def main():

        # Si hay tokens pendientes
        if len(tokens) > 0:

            token = tokens.pop(0) # Obtener siguiente token

            # Puede ser línea de control
            if token == tokenCode["controlLine"]:
                print("- Control Line")
                main()
            # Puede ser línea de datos y empezar con instrumento
            elif token == tokenCode["instrument"]:
                notes()
                main()
            # Si es otro token hay un error de sintaxis
            else:
                print("ERROR: Sintaxis no valida")
                quit()
        
        # La falta de tokens representa épsilon
        else:
            print("Parser ejecutado con exito...")


    # Módulo notes
    def notes():
        
        token = tokens.pop(0) # Obtener siguiente token

        # Puede ser nota
        if token == tokenCode["note"]:
            notes()
        # Puede ser barra
        elif token == tokenCode["bar"]:
            notes()
        # Puede ser newline y aquí se acepta notes
        elif token == tokenCode["newline"]:
            print("- Data Line")
        # Si es otro token hay un error de sintaxis
        else:
            print("ERROR: Sintaxis no valida")
            quit()


    # Ejecutar módulo main
    main()
        
