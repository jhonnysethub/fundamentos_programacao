idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário atual: "))
tempot = int(input("Digite seu tempo de trabalho em anos: "))
emprestimo = float(input("Digite o valor do empréstimo desejado: "))

if idade < 18:
    print("Empréstimo não permitido")

elif salario < 1500:
    print("Renda insuficiente")

elif tempot < 1:
    print("Tempo de trabalho insuficiente")

elif emprestimo == (salario * 10):
    print("Valor solicitado muito alto")

else:
    print("Empréstimo pré-aprovado")
