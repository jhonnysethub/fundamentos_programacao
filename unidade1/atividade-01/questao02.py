preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque desse produto: "))

if preco <= 0: 
    print("Preço inválido")

elif quantidade <= 0: 
    print("Quantidade inválida")

elif preco > 1000 and quantidade < 5:
    print("Produto caro com estoque crítico") 

elif preco > 1000 and quantidade <= 20:
    print("Produto caro com estoque normal") 

elif preco > 1000 and quantidade > 20:
    print("Produto caro com estoque alto") 

elif preco > 0 and quantidade < 5:
    print("Estoque crítico") 

elif preco > 0 and quantidade <= 20:
    print("Estoque normal") 
