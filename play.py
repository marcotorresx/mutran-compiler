# Imports
import re
import sounddevice as sd
import numpy as np

# Estructura para relacionar notenames con indice de tecla en piano
notenameNums = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11
}


# Estructura para relacionar tval con duración
tvalDurations = {
    "w": 4,
    "h": 2,
    "q": 1,
    "e": 0.5,
    "s": 0.25,
    "t": 0.125,
    "f": 0.0625
}


# Tocar las notas musicales encontradas en la archivo
def play(notes):

    for note in notes:

        # Obtener pitch
        pitchPattern = re.compile(r"^((A|B|C|D|E|F|G)(#+|b+)?(-2|-1|0|1|2|3|4|5|6|7|8)|R)")
        pitchRes = re.search(pitchPattern, note) # Buscar patrón en nota
        pitch = note[pitchRes.start():pitchRes.end()]

        # Buscar rest
        restPattern = re.compile(r"^R") # Comienza con R
        restRes = re.search(restPattern, pitch) # Buscar patrón en pitch

        # Si se encontró rest
        if restRes:
            frecuency = 0 # La frecuencia es 0

        # Si no se encontró rest obtener notename y octave
        else:

            # Obtener notename
            notenamePattern = re.compile(r"^(A|B|C|D|E|F|G)(#|b)?") # Para generar sonido se ignoran #/b extras
            notenameRes = re.search(notenamePattern, pitch) # Buscar patrón en pitch
            notename = note[notenameRes.start():notenameRes.end()]

            # Obtener octave
            octavePattern = re.compile(r"(-2|-1|0|1|2|3|4|5|6|7|8)")
            octaveRes = re.search(octavePattern, pitch) # Buscar patrón en pitch
            octave = note[octaveRes.start():octaveRes.end()]

            # Buscar número de nota para calcular frecuencia
            notenameNum = notenameNums.get(notename, None)

            # Si la nota no existe en el piano (E#, Fb, B#, Cb) marcar error
            if notenameNum == None:
                print("")
                print(f'ERROR: Notename "{notename}" no existe en piano')
                print("")
                quit()

            # Obtener la frecuencia
            frecuency = getFrecuency(notenameNum, int(octave))

        # Obtener tval
        tvalPattern = re.compile(r"(w|h|q|e|s|t|f)")
        tvalRes = re.search(tvalPattern, note) # Buscar patrón en nota
        tval = note[tvalRes.start():tvalRes.end()]
            
        # Obtener duración de tval
        duration = tvalDurations[tval]

        # Reproducir sonido de nota
        playSound(frecuency, duration)


# Calcular la frecuencia de una nota en una octava
def getFrecuency(notenameNum, octave):

    expo = ( octave - 4 ) * 12 + ( notenameNum - 9 )
    return 440 * ( (2 ** ( 1 / 12 ) ) ** expo )


# Reproducir sonido de nota
def playSound(frecuency, duration):

    # Datos
    frametime = 44100
    amplitude = np.linspace(0, duration, int(frametime * duration))
    wave = np.sin(2 * np.pi * frecuency * amplitude)

    # Reproducir sonido
    sd.play(wave, frametime)
    sd.wait()
