idade = int(input("Digite a idade do aluno: "))
media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite o percentual de frequência do aluno:"))
curso = int(input("\nQual o tipo de curso do aluno:\n1- Graduação\n2- Técnico\n3- Pós-graduação\n>> "))

if frequencia < 75:
    print("Aluno Reprovado.")

else:
    match curso:
        case 1:
            if media >= 7:
                print("Aluno Aprovado.")
        
            if media >= 5:
                print("Aluno Recuperação.")
            else:
                print("Aluno Reprovado.")
    
        case 2:
            if media >= 6:
                print("Aluno Aprovado.")

            if media >= 4:
                print("Aluno Recuperação.")

            else:
                print("Aluno Reprovado.")

        case 3:
            if media >= 7:
                print("Aluno Aprovado.")

            else:
                print("Aluno Reprovado.")
