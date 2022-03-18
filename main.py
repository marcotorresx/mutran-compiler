'''
Evidencia 1 - Implementación de Métodos Computacionales

Marco Antonio Torres Sepúlveda
A01025334
'''

# Importaciones
from scanner import scanner
from parser import parser
from play import play 

# Estructura para relacionar lexemas con tokens
tokenCode = {
    "controlLine": 100,
    "instrument": 101,
    "note": 102,
    "bar": 103,
    "newline": 104
}

# Función principal
def main():

    # Abrir archivo txt con canción en formato mutran
    songFile = open('song.txt', 'r')
    lines = songFile.readlines()

    # Ejecutar scanner y recibir lista de tokens
    print("")
    print("--- SCANNER ---")
    print("Lexemas reconocidos:")
    tokens, notes = scanner(lines, tokenCode)

    # Ejecutar parser y verificar sintaxis
    print("")
    print("--- PARSER ---")
    print("Sintaxis reconocida:")
    parser(tokens, tokenCode)

    # Tocar las notas musicales
    print("")
    print("--- CANCION ---")
    print("Tocando cancion...")
    print("")
    play(notes)
    

main()