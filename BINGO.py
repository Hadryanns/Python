import random

valores_nao = ['NAO', 'NÃO', 'N', 'NO', '0', 'NN', 'NA', 'NAM']
valores_sim = ['SIM', 'SIN', 'S', 'YES', '1', 'SS', 'SI']

#SORTEAR NUMEROS

numerosLista = []
cont = 75
numeroMaximo = 75
while cont > 0:
    numeroSorteado = random.randint(1,numeroMaximo)
    while numeroSorteado not in numerosLista:
        if numeroSorteado not in numerosLista:
            numerosLista.append(numeroSorteado)
            cont -= 1

#FAZER TABELA

tabela = [   ["B"]
            ,["I"]
            ,["N"]
            ,["G"]
            ,["O"]]
for a,coluna in enumerate(tabela):
    if coluna[0] == "B":
        novaLista=random.sample(range(1,16),5)
        tabela[a]=tabela[a]+novaLista
    elif coluna[0] == "I":
        novaLista=random.sample(range(16,31),5)
        tabela[a]=tabela[a]+novaLista
    elif coluna[0] == "N":
        novaLista=random.sample(range(31,46),5)
        tabela[a]=tabela[a]+novaLista
    elif coluna[0] == "G":
        novaLista=random.sample(range(46,61),5)
        tabela[a]=tabela[a]+novaLista
    elif coluna[0] == "O":
        novaLista=random.sample(range(61,76),5)
        tabela[a]=tabela[a]+novaLista
print("\nTABELA COMPLETA QUE COMEÇE OS JOGOS\n")
print('\n'.join(map(str,tabela)))

#PERGUNTA AO USUÁRIO

contagens = 0
pedirNumero = input("\nDeseja um número(S/N)? ")
while contagens < numeroMaximo and numerosLista:
    if pedirNumero.upper() in valores_sim:
        if numerosLista[contagens] >= 1 and numerosLista[contagens] <= 15:
            print(f"O número sorteado foi {numerosLista[contagens]} - B")
            if numerosLista[contagens] in tabela[0]:
                print("\nTABELA ATUALIZADA\n")
                indiceDeTroca=tabela[0].index(numerosLista[contagens])
                tabela[0][indiceDeTroca] = "X"
                print('\n'.join(map(str,tabela)))
        if numerosLista[contagens] >= 16 and numerosLista[contagens] <= 30:
            print(f"O número sorteado foi {numerosLista[contagens]} - I")
            if numerosLista[contagens] in tabela[1]:
                print("\nTABELA ATUALIZADA\n")
                indiceDeTroca=tabela[1].index(numerosLista[contagens])
                tabela[1][indiceDeTroca] = "X"
                print('\n'.join(map(str,tabela)))
        if numerosLista[contagens] >= 31 and numerosLista[contagens] <= 45:
            print(f"O número sorteado foi {numerosLista[contagens]} - N")
            if numerosLista[contagens] in tabela[2]:
                print("\nTABELA ATUALIZADA\n")
                indiceDeTroca=tabela[2].index(numerosLista[contagens])
                tabela[2][indiceDeTroca] = "X"
                print('\n'.join(map(str,tabela)))
        if numerosLista[contagens] >= 46 and numerosLista[contagens] <= 60:
            print(f"O número sorteado foi {numerosLista[contagens]} - G")
            if numerosLista[contagens] in tabela[3]:
                print("\nTABELA ATUALIZADA\n")
                indiceDeTroca=tabela[3].index(numerosLista[contagens])
                tabela[4][indiceDeTroca] = "X"
                print('\n'.join(map(str,tabela)))
        if numerosLista[contagens] >= 61 and numerosLista[contagens] <= 75:
            print(f"O número sorteado foi {numerosLista[contagens]} - O")
            if numerosLista[contagens] in tabela[4]:
                print("\nTABELA ATUALIZADA\n")
                indiceDeTroca=tabela[4].index(numerosLista[contagens])
                tabela[4][indiceDeTroca] = "X"
                print('\n'.join(map(str,tabela)))
        print()
        contagens += 1    
        if contagens<numeroMaximo:
            pedirNumero = input("Deseja outro número(S/N)? ")
        else:
            print("Fim de Jogo")
            contagens = 75
    if pedirNumero.upper() in valores_nao:
        print("Fim de Jogo")
        contagens = 75