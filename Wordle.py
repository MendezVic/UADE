# 1-Crear y leer un archivo en base a Tuplas donde existen ciertas palabras
# y devuelva aleatoriamente una de esas. (Ahí aplicamos funciones, cadena de
# caracteres, archivos y tuplas)
import random
from colorama import Fore, Back, Style, init

def elegir_palabra():
    arch = open("Palabras.txt", "r")
    palabras = []
    linea = arch.readline()

    while linea:
        palabra = linea.rstrip("\n")
        palabras.append(palabra)
        linea = arch.readline()
    numero_aleatorio = random.randrange(0, len(palabras))

    return palabras[numero_aleatorio].upper()



def pedir_palabra(palabras_adivinadas):
    try:
        palabra = input("Ingrese una palabra de 5 letras: ").upper()
        if len(palabra) != 5:
            raise ValueError
        assert palabra not in palabras_adivinadas

    except AssertionError:
        print(f"{Fore.YELLOW}Ya ingresaste esta palabra antes", end="\n")
        palabra = pedir_palabra(palabras_adivinadas)
    except ValueError:
        print(f"{Fore.RED}ERROR, la palabra debe tener 5 letras", end="\n")
        palabra = pedir_palabra(palabras_adivinadas)

    return palabra.upper()


def revisar_palabra(palabra, palabra_correcta):
    mapa = []
    palabras_mostrar = []
    i = 0
    for letter in palabra:
        if palabra[i] == palabra_correcta[i]:
            mapa.append(COLORES["LUGAR_CORRECTO"])
            palabras_mostrar.append(f"{Fore.GREEN}{letter}")

        # palabra que coincide con la palabra pero no posicion (amarillo)
        elif palabra[i] in palabra_correcta:
            mapa.append(COLORES["LETRA_CORRECTA"])
            palabras_mostrar.append(f"{Fore.YELLOW}{letter}")
        # palabra que no coincide con ninguna de las dos (rojo)
        else:
            mapa.append(COLORES["LETRA_INCORRECTA"])
            palabras_mostrar.append(f"{Fore.RED}{letter}")
        i += 1

    return mapa, palabras_mostrar


def juego(palabra_correcta):
    fin_de_juego = False
    palabras_adivinadas = []
    todos_los_mapas = []
    todas_las_palabras_mostrar = []
    palabra = ""

    while not fin_de_juego:
        palabra = pedir_palabra(palabras_adivinadas)
        palabras_adivinadas.append(palabra)

        mapa_de_intentos, palabra_mostrar = revisar_palabra(palabra, palabra_correcta)
        todos_los_mapas.append(mapa_de_intentos)
        todas_las_palabras_mostrar.append(palabra_mostrar)

        for i in range(len(todas_las_palabras_mostrar)):
            print("".join(todas_las_palabras_mostrar[i]), end="\n")
        if palabra == palabra_correcta or len(palabras_adivinadas) == 6:
            fin_de_juego = True
        print(Style.RESET_ALL)
    for mapa in todos_los_mapas:
        print("".join(mapa), end="\n")
    if len(palabras_adivinadas) == 6 and palabra != palabra_correcta:
        print(f"{Fore.RED}Te quedaste sin intentos", end="\n")
        print(f"{Style.RESET_ALL}La palabra correcta era{Fore.GREEN} {palabra_correcta}", end="\n")
    else:
        print(f"!!Adivinaste la palabra correcta es{Fore.GREEN} {palabra_correcta}!! ", end="\n")



COLORES = {
    "LUGAR_CORRECTO": "🟩",
    "LETRA_CORRECTA": "🟨",
    "LETRA_INCORRECTA": "🟥"
}


def main():
    init()
    palabra_random = elegir_palabra()
    print(palabra_random)
    print("Bienvenido a Wordle", end="\n")
    juego(palabra_random)


main()
