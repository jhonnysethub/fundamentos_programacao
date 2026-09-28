n = int(input("Quantas vezes vai repetir: "))
menor = maior = int(input("Digite o 1º valor: "))
soma = 0

for i in range(2, n+1):
    v = int(input(f"Digite o {i}º valor: "))
    soma += v
    
    if v > maior:
        maior = v
    if v < menor:
        menor = v

media = soma / n
print(f"\nSoma: {soma}\nMédia: {media:.1f}\nMaior: {maior}\nMenor: {menor}")

# usando lista

# numeros = []
# rep = int(input("Digite quantos valores serão: "))

# for i in range(rep):
#     v = int(input(f"Digite o {i+1}º valor: "))
#     numeros.append(v)

# soma = sum(numeros)
# media = soma / rep
# maior = max(numeros)
# menor = min(numeros)

# print(f"\nSoma: {soma}\nMédia: {media:.1f}\nMaior: {maior}\nMenor: {menor}")