import re

# Escanear las líneas del texto y generar tokens
def scanner(lines, tokenCode):

    tokens = [] # Lista de tokens
    notes = [] # Lista de notas

    for line in lines:

        # Checar si es una linea de control
        controlLinePattern = re.compile(r"^#.+$") # Patrón que primer caractér sea #
        isControlLine = bool(re.search(controlLinePattern, line.strip())) # Buscar patrón en linea

        # Si es linea de control
        if isControlLine:
            print("- Control Line")
            tokens.append(tokenCode["controlLine"]) # Agrega token
            continue # Pasa a la siguiente linea

        # Generar array diviendo la linea por espacios
        items = line.split()

        # Checar que cada elemento corresponda con una expresión regular válida
        for item in items:

            # Checar si es una nota
            notePattern = re.compile(r"^((A|B|C|D|E|F|G)(#+|b+)?(-2|-1|0|1|2|3|4|5|6|7|8)|R)(w|h|q|e|s|t|f)(\.+|(t|3|5|7|9))?$")
            isNote = bool(re.search(notePattern, item)) # Buscar patrón en linea

            # Checar si es un instrumento
            instrumentPattern = re.compile(r"^[a-z]+$") # Una o más letras minúscula y mayúscula
            isInstrument = bool(re.search(instrumentPattern, item)) # Buscar patrón en linea

            # Checar si es una barra vertical
            barPattern = re.compile(r"^\|$") # Una barra vertical
            isBar = bool(re.search(barPattern, item)) # Buscar patrón en linea

            # Si es nota
            if isNote:
                print("- Note")
                tokens.append(tokenCode["note"]) # Agrega token
                notes.append(item) # Agrega nota

            # Si es instrumento
            elif isInstrument:
                print("- Instrument")
                tokens.append(tokenCode["instrument"]) # Agrega token
            
            # Si es barra
            elif isBar:
                print("- Bar")
                tokens.append(tokenCode["bar"]) # Agrega token

            # Si es otro
            else:
                print("")
                print(f'ERROR: Lexema no valido "{item}"') # Imprimir expresion no valida
                print("")
                quit() # Salir del programa

        # Cuando recorre todos los elementos de la línea de datos agrega token newline
        print("- New Line")
        tokens.append(tokenCode["newline"])

    print("Scanner ejecutado con exito...")
    return tokens, notes