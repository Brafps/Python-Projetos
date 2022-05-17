# Definição de operações

def soma():
    print("Digite os números que deseja efetuar a soma:")
    f_soma = 0.0
    i_contador = 0
    while True:    
        s_num_flash = input()
        if s_num_flash == ("s" or "S"):
            break
        elif type(float(s_num_flash)) == type(0.0):
            f_soma += float(s_num_flash)
            i_contador += 1
            if i_contador>=2:
                print("Digite S a qualquer momento para ter o resultado da soma ou digite um novo valor.")
    print("-----------------------------------------------")
    return f_soma

def diferença():
    f_minuendo = float(input("Digite o valor do minuendo:"))
    f_subtraendo = float(input("Digite o valor do subtraendo:"))
    print("-----------------------------------------------")
    return f_minuendo - f_subtraendo

def produto():
    print("Digite os números que deseja efetuar o produto:")
    f_produto = 1.0
    i_contador = 0
    while True:    
        s_num_flash = input()
        if s_num_flash == ("s" or "S"):
            break
        elif type(float(s_num_flash)) == type(0.0):
            f_produto = f_produto*float(s_num_flash)
            i_contador += 1
            if i_contador>=2:
                print("Digite S a qualquer momento para ter o resultado da soma ou digite um novo valor.")
    print("-----------------------------------------------")
    return f_produto


def divisao():
    f_dividendo = float(input("Digite o valor do dividendo:"))
    f_divisor = float(input("Digite o valor não nulo para o divisor:"))
    print("-----------------------------------------------")
    return f_dividendo/f_divisor

def f_m_aritmetica():
    print("Digite os números que deseja efetuar a média:")
    f_soma = 0.0
    i_contador = 0
    while True:    
        s_num_flash = input()
        if s_num_flash == ("s" or "S"):
            break
        elif type(float(s_num_flash)) == type(0.0):
            f_soma += float(s_num_flash)
            i_contador += 1
            if i_contador>=2:
                print("Digite S a qualquer momento para ter o resultado ou digite um novo valor.")
    print("-----------------------------------------------")
    return f_soma/i_contador

while True:
# Tela FIxa

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~ Calculadora em Python ~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n''')

    print("Abaixo, digite o valor da operação correspondente.\n")

#menus

    print('''[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Média Aritmética
[6] - Média Ponderada
[0] - Encerrar\n''')

    while True:
        i_operação = int(input("Qual operação deseja?\n"))
        if i_operação >= 0 and i_operação <= 9:
            break
        else:
            print("\033[0;31m Erro! Digite um valor de operação válido.\033[m")
# Condições

    if (i_operação == 1):
        print("-----------------------------------------------")
        print("A Soma dos números digitados é: %f" %soma())
        print("-----------------------------------------------\n")

    if (i_operação == 2):
        print("-----------------------------------------------")
        print("A diferença dos números digitados é: %f" %diferença())
        print("-----------------------------------------------\n")        
    
    if (i_operação == 3):
        print("-----------------------------------------------")
        print("O produto dos números digitados é: %f" %produto())
        print("-----------------------------------------------\n")

    if (i_operação == 4):
        print("-----------------------------------------------")
        print("O quociente dos números digitados é: %f" %divisao())
        print("-----------------------------------------------\n")

    if (i_operação == 5):
        print("-----------------------------------------------")
        print("A média aritmética dos números digitados é: %f" %f_m_aritmetica())
        print("-----------------------------------------------\n")

    if (i_operação == 6):
        print("-----------------------------------------------")
        print("Falta definir essa operação")
        print("-----------------------------------------------\n")

# Condição para finalizar o programa 
   
    elif (i_operação == 0):
        print("Finalizando...")
        break
 