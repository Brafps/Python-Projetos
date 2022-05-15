# Definição de operações

def soma(a,b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

# Início do Programa

print("~~~~~~ Calculadora em Python ~~~~~~\n")

print("Abaixo, digite o valor da operação correspondente.\n ")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão\n")


# Verificador da operação digitada

while True:
    operação = int(input("Qual operação deseja?\n"))
    if operação > 0 and operação < 5:
        break
    else:
        print("Você não digitou uma operação válida!\n")

# Entrada dos valores

i_num_1 = int(input("Digite o primeiro número:"))
i_num_2 = int(input("Digite o segundo número:"))


# Condicionais

if (operação == 1):
    print("\n {} + {} = {}".format(i_num_1, i_num_2, soma(i_num_1, i_num_2)))
elif (operação == 2):
    print("\n {} - {} = {}".format(i_num_1, i_num_2, sub(i_num_1, i_num_2)))
elif (operação == 3):
    print("\n {} * {} = {}".format(i_num_1, i_num_2, mult(i_num_1, i_num_2)))
else:
    print("\n {} / {} = {}".format(i_num_1, i_num_2, div(i_num_1, i_num_2)))