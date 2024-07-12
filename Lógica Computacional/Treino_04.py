import random
print("JOGO DO PALPITE")
print("""
      REGRAS:
      1-O computador gerará um número aléatorio a cada jogada, o objetivo do usuário é adivinhar qual número o computador gerou
      2-O número gerado sempre será inteiro, maior que 0 e menor 101
      3-O programa será encerrado quando usuário acertar o número gerado ou digitar o número 0

      Boa Sorte!
      """)
tentativa=0
cont=1
while cont>0:
    numero_aleatorio=random.randint(1,100)
    numero_usuario=int(input("Palpite um número entre 1 e 100: "))
    if numero_usuario==0:
        cont=0
    elif numero_usuario>=1 and numero_usuario<=100:
        if numero_usuario == numero_aleatorio:
            tentativa+=1
            print(f"Parabéns, você acertou o número com {tentativa} tentativas")
            cont=0
        else:
            print("Tente novamente")
            tentativa+=1
    elif numero_usuario>100:
        tentativa+=1
        print("ERROR: Digite um número menor ou igual a 100")
if tentativa==0:
    print("Nem tentou")
print("Fim do programa")