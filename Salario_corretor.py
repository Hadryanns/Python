qtd_vendas=int(input("Quantidade de imóveis vendidos: "))
salario=1500.00
total=qtd_vendas*200+salario
while qtd_vendas>0:
    casa=float(input(f"Valor do imóvel: R$"))
    casa=casa*0.05
    total+=casa
    qtd_vendas-=1
    # print(f"{total}")
print(f"O corretor esse mês ganhou R${total:.2f}")