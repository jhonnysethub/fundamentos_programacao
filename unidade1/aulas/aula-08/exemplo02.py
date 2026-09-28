lista = []
ordem = int(input("Quantos números tem na sua lista: "))

for i in range(ordem):
    n = int(input(f"Digite o {i+1}º item da lista: "))
    lista.append(n)

print(lista)