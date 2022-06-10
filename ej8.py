def esbisiesto(año):
    if (año % 4) != 0:
        return False
    elif (año % 4) == 0 and (año % 100) == 0 and (año % 400) != 0:
        return True
    elif (año % 4) == 0 and (año % 100) != 0:
        return True
    elif (año % 4) == 0 and (año % 100) == 0 and (año % 400) == 0:
        return True


def diasenmes(mes, año):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return 31
    if mes == 2:
        if esbisiesto(año):
            return 29
        return 28
    return 30


def diadelasemana(dia, mes, año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def printcalendar(mes, año):
    print("Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa")
    primerdia = diadelasemana(1, mes, año)
    diasmes = diasenmes(mes, año)
    for j in range(primerdia):
        print(" ", end="  ")
    i = 1
    while i <= diasmes:
        if i < 10:
            print(i, end="  "),
        else:
            print(i, end=" ")
        if (i + primerdia) % 7 == 0:
            print(" ")
        i += 1


mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))

printcalendar(mes, año)
