n = int(input("Quantas vezes vai repetir: "))
menor = maior = int(input("Digite o 1º valor: "))

for i in range(2, n+1):
    v = int(input(f"Digite o {i}º valor: "))
    
    if v > maior:
        maior = v
    if v < menor:
        menor = v

print(f"\nMaior: {maior}\nMenor: {menor}\nDiferença: {maior - menor}")