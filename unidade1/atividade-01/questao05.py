np = float(input("Digite sua nota de produtividade: "))
nq = float(input("Digite sua nota de qualidade: "))
presenca = float(input("Digite seu percentual de presença: "))

media = (np + nq)/2

print(f"\nMédia: {media:.1f} Presença: {presenca:.1f}%")

if presenca < 75: 
    print("Desempenho comprometido por baixa frequência")
else:
    if media >= 9 and presenca >= 90:
        print("Desempenho Excelente")

    elif media >= 7 and presenca >= 85:
        print("Desempenho Bom")

    elif media >= 5 and presenca >= 75:
        print("Desempenho Regular")

    else:
        print("Desempenho Insatisfatório")