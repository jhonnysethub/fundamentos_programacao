nota = float(input("Digite a nota do 1º aluno: "))
aprovados = 0
recuperados = 0
reprovados = 0
total = 0

while nota > -1:
    total += 1
    nota = float(input("Digite a nota do próximo aluno: "))
    
    if nota > 5:
        if nota >= 7:
            aprovados += 1
        else:
            recuperados += 1
    else:
        reprovados += 1

print(f"\nTotal de alunos: {total}\nAprovados: {aprovados}\nRecuperação: {recuperados}\nReprovados: {reprovados}")