produto1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o preço do primeiro produto: R$ "))
quantidade1 = int(input("Digite a quantidade do primeiro produto: "))

produto2 = input("Digite o nome do segundo produto: ")
preco2 = float(input("Digite o preço do segundo produto: R$ "))
quantidade2 = int(input("Digite a quantidade do segundo produto: "))

produto3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input("Digite o preço do terceiro produto: R$ "))
quantidade3 = int(input("Digite a quantidade do terceiro produto: "))

total1 = preco1 * quantidade1
total2 = preco2 * quantidade2
total3 = preco3 * quantidade3

final = total1 + total2 + total3

print(f"\nProdutos comprados e valores:\n {produto1}: {quantidade1} x R$ {preco1:.2f} = R$ {total1:.2f} \n {produto2}: {quantidade2} x R$ {preco2:.2f} = R$ {total2:.2f}\n {produto3}: {quantidade3} x R$ {preco3:.2f} = R$ {total3:.2f} \n TOTAL GERAL: R$ {final:.2f}")