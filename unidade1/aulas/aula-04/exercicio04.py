n = float(input("Digite sua nota: "))
f = float(input("Digite a porcentagem de sua frequência (sem símbolo): "))

aprovado = n >= 7.0 and f >= 75

print(f"Considerando sua nota({n:.1f}) e frequência({f:.1f}%), sua aprovação foi: {aprovado}")