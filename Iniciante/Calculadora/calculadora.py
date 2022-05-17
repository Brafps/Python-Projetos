# Definição de operações

def soma():
    lista = []
    contador = 1
    while True:    
            f_num_flash = input(f"Digite o #{contador} número ou S para sair desse menu:")
            if f_num_flash == ("s" or "S"):
                break
            elif f_num_flash.isnumeric():
                lista.append(float(f_num_flash))
                contador += 1

            else:
                print("\033[0;31m Erro! Digite um valor de operação válido.\033[m")
    return print("A Soma dos números digitados é igual a: %f\n" %sum(lista))

# Tela FIxa

print("~~~~~~ Calculadora em Python ~~~~~~\n")

print("Abaixo, digite o valor da operação correspondente. ")

while True:
    print('''[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Média Aritmética
[6] - Média Ponderada
[0] - Encerrar''')

    while True:
        operação = int(input("\nQual operação deseja?\n"))
        if operação >= 0 and operação <= 9:
            break
        else:
            print("\033[0;31m Erro! Digite um valor de operação válido.\033[m")
# Condições

    if (operação == 1):
        soma()

# Condição para finalizar o programa 
        
    
    elif (operação == 0):
        print("Finalizando...")
        break
 