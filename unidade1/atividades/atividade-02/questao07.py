print("Você vai digitar 10 números inteiros ou positivos")
positivos = 0
zeros = 0
negativos = 0

for i in range (10):
    v = int(input(f"Digite o {i+1}º valor: "))
    
    if v > 0:
        positivos += 1
    if v == 0:
        zeros += 1
    if v < 0:
        negativos += 1

print(f"\nPositivos: {positivos}\nNegativos: {negativos}\nZeros: {zeros}")