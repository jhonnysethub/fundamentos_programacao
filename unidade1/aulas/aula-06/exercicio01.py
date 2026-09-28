soma = 0

for i in range(1,4):
    n = int(input(f"Digite seu {i}º valor: "))
    soma += n

media = soma / i
print(f"A média aritmética dos seus valores é: {media:.1f}")
