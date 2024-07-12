import random
print("JOGO DO DADO")
cont=int(input("Digite 0 para encerrar o programa ou 1 para girar o dado: "))
while cont == 1:
    numero_sorteado=random.randint(1,6)
    print(numero_sorteado)
    cont=int(input("Digite 0 para sair ou 1 para girar novamente o dado: "))
print("Fim do programa")