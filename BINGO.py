import random,pprint
numerosLista = []
valores_nao = ['NAO', 'NÃO', 'N', 'NO', '0', 'NN', 'NA', 'NAM']
valores_sim = ['SIM', 'SIN', 'S', 'YES', '1', 'SS', 'SI']
cont = 75
numeroMaximo = 75
while cont > 0:
    numeroSorteado = random.randint(1,numeroMaximo)
    while numeroSorteado not in numerosLista:
        if numeroSorteado not in numerosLista:
            numerosLista.append(numeroSorteado)
            cont -= 1
contagens = 0
pedirNumero = input("Deseja um número(S/N)? ")
while contagens < numeroMaximo and numerosLista:
    if pedirNumero.upper() in valores_sim:
        if numerosLista[contagens] >= 1 and numerosLista[contagens] <= 15:
            print(f"O número sorteado foi {numerosLista[contagens]} - B")

        if numerosLista[contagens] >= 16 and numerosLista[contagens] <= 30:
            print(f"O número sorteado foi {numerosLista[contagens]} - I")

        if numerosLista[contagens] >= 31 and numerosLista[contagens] <= 45:
            print(f"O número sorteado foi {numerosLista[contagens]} - N")

        if numerosLista[contagens] >= 46 and numerosLista[contagens] <= 60:
            print(f"O número sorteado foi {numerosLista[contagens]} - G")

        if numerosLista[contagens] >= 61 and numerosLista[contagens] <= 75:
            print(f"O número sorteado foi {numerosLista[contagens]} - O")
        contagens += 1    
        if contagens<numeroMaximo:
            pedirNumero = input("Deseja outro número(S/N)? ")
        else:
            print("Fim de Jogo")
            contagens = 75
    if pedirNumero.upper() in valores_nao:
        print("Fim de Jogo")
        contagens = 75
pprint([[1,2,3][4,5,6,][7,8,9]])