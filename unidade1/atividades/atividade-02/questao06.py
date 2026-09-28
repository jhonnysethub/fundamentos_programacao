senha = "1234"
tentativa = input("Digite a senha: ")

while tentativa != senha:
    tentativa = input("Incorreto. Tente Novamente: ")

print("Acesso autorizado!")