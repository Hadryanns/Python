qnt=0
valor=0
print("CODE          NOME            VALOR")
print(" 1       Cachorro Quente    R$ 4.00")
print(" 2          X-Salada        R$ 4.50")
print(" 3           X-Bacon        R$ 5.00")
print(" 4       Torrada Simples    R$ 2.00")
print(" 5         Refrigerante     R$ 1.50")
itens=int(input("Digite a quantidade de itens únicos que deseja comprar: "))
while itens >0:
    codigo=int(input("Digite o codigo do ítem: "))
    qnt = int(input("Digite a quantidade que voce deseja: "))
    if codigo==1:
        valor+=qnt*4
    elif codigo==2:
        valor+=qnt*4.50 
    elif codigo==3:
        valor+=qnt*5
    elif codigo==4:
        valor+=qnt*2
    elif codigo==5:
        valor+=qnt*1.5
    itens-=1
print(f"A compra total custou R$ {valor:.2f}")