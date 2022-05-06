print("~~~~~~ Calculadora em Python ~~~~~~\n")

print("Abaixo, digite o valor da operação correspondente.\n ")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão\n")

while True:
    operação = int(input("Qual operação deseja?\n"))
    if operação > 0 and operação < 5:
        break
    else:
        print("Você não digitou uma operação válida!\n")


i_num_1 = int(input("Digite o primeiro número:"))
i_num_2 = int(input("Digite o segundo número:"))

if (operação == 1):
    soma = i_num_1 + i_num_2
    print("\n {} + {} = {}".format(i_num_1, i_num_2, soma))
elif (operação == 2):
    subtracao = i_num_1 - i_num_2
    print("\n {} - {} = {}".format(i_num_1, i_num_2, subtracao))
elif (operação == 3):
    multiplicacao = i_num_1 * i_num_2
    print("\n {} * {} = {}".format(i_num_1, i_num_2, multiplicacao))
elif (operação == 4):
    divisao = i_num_1 / i_num_2
    print("\n {} / {} = {}".format(i_num_1, i_num_2, divisao))



