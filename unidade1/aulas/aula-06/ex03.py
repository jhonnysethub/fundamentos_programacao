numeros = ""

for i in range(1,11):
    para_str = str(i)
    if i != 10:
        para_str += ", "

    numeros += para_str

print(numeros)