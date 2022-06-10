# camiones peso max 500.000 gramos
# naranjas entre 200 y 300 gramos
# cajon entran 100 naranjas
import random

CAMION_MAX = 500000
CAJA_MAX = 100


def calcular_camiones(peso_total_naranjas):
    nro_camion = peso_total_naranjas // CAMION_MAX
    naranjas_restantes = peso_total_naranjas % CAMION_MAX

    if (naranjas_restantes >= (80 * CAMION_MAX / 100)):
        nro_camion += 1
        naranjas_restantes = 0
    naranjas_restantes = naranjas_restantes / 1000
    return nro_camion, naranjas_restantes

def calcular_naranjas_sin_caja(nro_naranjas, naranjas_para_jugo, nro_cajas):
    return nro_naranjas - naranjas_para_jugo - (nro_cajas * 100)

def calcular(nro_naranjas):
    nro_cajas = 0
    peso_total_naranjas = 0
    naranjas_en_caja = 0
    naranjas_para_jugo = 0
    for naranja in range(nro_naranjas):
        peso_naranja = random.randrange(150, 350)

        if (peso_naranja < 200 or peso_naranja > 300):
            naranjas_para_jugo += 1
            continue
        else:
            naranjas_en_caja += 1
            peso_total_naranjas += peso_naranja

        if (naranjas_en_caja == CAJA_MAX):
            nro_cajas += 1
            naranjas_en_caja = 0
    nro_camion, naranjas_restantes = calcular_camiones(peso_total_naranjas)
    naranjas_fuera_de_caja = calcular_naranjas_sin_caja(nro_naranjas, naranjas_para_jugo, nro_cajas)

    print(f"Se deben llenar {nro_cajas} cajones.")
    print(f"Hay {naranjas_para_jugo} naranjas para jugo")
    if (nro_camion > 0):
        print(f"Se necesitan {nro_camion} camiones para transportar la cosecha")
    else:
        print("No se puede alcanzar ocupacion requerida para el camion del 80%")
    print(f"Quedan {naranjas_restantes} kilogramos de naranjas para el siguiente envio")


naranjas = int(input("Ingresar cantidad de naranjas: "))

calcular(naranjas)
