nome = input("Digite seu nome: ")

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

media = (n1 + n2 + n3)/3

if media >= 7:
    print(f"{nome}, você foi aprovado chefe👌") 

else:
    print(f"{nome}, você foi reprovado irmão, tem que estudar😶‍🌫️") 