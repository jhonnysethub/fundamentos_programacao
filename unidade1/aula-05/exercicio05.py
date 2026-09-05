salario = float(input("Digite seu salário: R$"))

if salario <= 1500:
    percentual = 1.15

elif salario > 1500 and salario <= 3000:
    percentual = 1.10

elif salario > 3000 and salario <= 5000:
    percentual = 1.07

else:
    percentual = 1.05
    
porcentagem = (percentual - 1) * 100
novo = salario * percentual
aumento = novo - salario

print(f"Salário inicial: R${salario:.2f} \nPercentual de aumento: {porcentagem:.2f}% \nValor do Aumento: R${aumento:.2f} \nNovo Salário: R${novo:.2f}")