import re

# Abrir archivo txt con canción en formato mutran
songFile = open('test.txt', 'r')
lines = songFile.readlines()


for line in lines:

    controlLinePattern = re.compile(r"^#.+$") # Patrón que primer caractér sea #
    isControlLine = bool(re.search(controlLinePattern, line)) # Buscar patrón 

    print(line, isControlLine)