def capicuas(lista):
    lista_reverso = lista[:]
    lista_reverso.reverse()
    valor_return = True
    for i in range(len(lista)):
        if lista[i] != lista_reverso[i]:
            valor_return = False
            break
    return valor_return


lista_general = [1, 2, 8, 2]
lista_capicua = capicuas(lista_general)
print(f"Si la lista es capicua, se mostrara TRUE, si no, sera FALSE: {lista_capicua}")
