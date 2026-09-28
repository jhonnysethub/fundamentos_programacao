n = input("Digite seu nome: ")
idade = int(input(f"Digite sua idade, {n}: "))

if idade <= 0:
    print(f"Idade inválida, {n}.")
    
elif idade <= 12:
    print(f"Você é uma Criança, {n}.")

elif idade < 18:
    print(f"Você é um(a) Adolescente, {n}.")

elif idade < 60:
    print(f"Você é um(a) Adulto(a), {n}.")

else:
    print(f"Você é um(a) Idoso(a), {n}.")

