I_limite_sup = int(input("Digite um número para encontrar todos os primos até ele:"))

for i in range(2, I_limite_sup + 1):
    j = 2
    contador = 0
    while j < i:
        if i % j == 0:
            contador = 1
            j = j + 1
        else:
            j = j + 1
    if contador == 0:
        print(str(i) + " é um número primo.")
        contador = 0
    else:
        contador = 0
