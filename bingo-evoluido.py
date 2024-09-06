import random,pprint
numeroMaximo = 75
def SortearNumeros(MaxNumber):
    numerosLista = []
    cont = 75
    MaxNumber = 75
    while cont > 0:
        numeroSorteado = random.randint(1,MaxNumber)
        while numeroSorteado not in numerosLista:
            if numeroSorteado not in numerosLista:
                numerosLista.append(numeroSorteado)
                cont -= 1
