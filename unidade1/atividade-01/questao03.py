media = float(input("Digite sua média acadêmica: "))
frequencia = float(input("Digite seu percentual de frequência: "))
rendaf = float(input("Digite sua renda familiar: "))
bolsa = input("Você já possui bolsa? [S/N]: ").upper()

if bolsa == "S": bolsa = True
else: bolsa = False
   
if media >= 7 and frequencia >= 75 and rendaf <= 3000 and bolsa == False:
    print("Você é elegível")

else:
    print("Você não é elegível para bolsa. Impedimentos(o):\n")
    if media < 7: 
        print(f">> Sua média ({media:.1f}) é menor que a desejada(7.0)")
    
    if frequencia < 75: 
        print(f">> Seu percentual de frequência ({frequencia:.1f}%) é menor que o desejado(75%)")
        
    if rendaf > 3000: 
        print(f">> Sua renda familiar (R${rendaf:.2f}) é maior que a esperada(R$3000.00)")
    
    if bolsa == True: 
        print(f">> Você já possui uma Bolsa")
