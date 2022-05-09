# Definição de operações

def soma(a,b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

def media(lista):
    soma = sum(lista)
    tamanho = len(lista)
    return soma/tamanho




print("~~~~~~ Calculadora em Python ~~~~~~\n")

print("Abaixo, digite o valor da operação correspondente.\n ")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão\n")
print("5 - Média Aritmética")

while True:
    operação = int(input("Qual operação deseja?\n"))
    if operação > 0 and operação < 5:
        break
    else:
        print("Você não digitou uma operação válida!\n")


if (operação == 1):
    i_num_1 = int(input("Digite o primeiro número:"))
    i_num_2 = int(input("Digite o segundo número:"))
    print("\n {} + {} = {}".format(i_num_1, i_num_2, soma(i_num_1, i_num_2)))
elif (operação == 2):
    i_num_1 = int(input("Digite o primeiro número:"))
    i_num_2 = int(input("Digite o segundo número:"))
    print("\n {} - {} = {}".format(i_num_1, i_num_2, sub(i_num_1, i_num_2)))
elif (operação == 3):
    i_num_1 = int(input("Digite o primeiro número:"))
    i_num_2 = int(input("Digite o segundo número:"))
    print("\n {} * {} = {}".format(i_num_1, i_num_2, mult(i_num_1, i_num_2)))
elif (operação == 4):
    i_num_1 = int(input("Digite o primeiro número:"))
    i_num_2 = int(input("Digite o segundo número:"))
    print("\n {} / {} = {}".format(i_num_1, i_num_2, div(i_num_1, i_num_2)))
elif (operação == 5):
    while True:
        contador = 1
        soma += int(input("Digite o # {} número".format(contador)))
        
else:
    print("Você digitou uma operação inválida!")


