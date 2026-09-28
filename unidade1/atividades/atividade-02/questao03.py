n = int(input("Digite um número inteiro positivo qualquer: "))
soma = 0

for i in range(n+1):
    print(f"Soma = {soma} + {i}")
    soma += i

print(soma)