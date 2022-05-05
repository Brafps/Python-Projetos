'''
Definindo funções e métodos para usar na calculadora
'''

#Vefificador de núemros inteiros
def verificadorInt(men):
    b_ok = False
    i_valor = 0
    while True:
        n = str(input(men))
        if n.isnumeric():
            i_valor = int(n)
            b_ok = True
        else:
            print("\033[0;31m Erro! Digite um valor de operação válido.\033[m")
        if b_ok:
            break
    return i_valor

#Verificador de primalidade de número
def testPrimo(num):
    num_div = 0
    for i in range(1, num +1):
        if (num % i == 0):
            num_div += 1
    if num_div == 2:
        return print("O número %d é primo" %num)
    else:
        return print("O número %d não é primo" %num)

