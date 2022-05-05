'''
Definindo funções e métodos para usar na calculadora
'''

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