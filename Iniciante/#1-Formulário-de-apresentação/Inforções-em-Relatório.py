
'''
Variáveis
'''

nome = input("Escreva seu nome completo:")
cpf = input("Escreva seu cpf:")
end = input("Escreva seu endereço:")
idade = int(input("Escreva sua idade:"))
altura = float(input("Escreva sua altura:"))
ddd = input("Escreva seu DDD:")
fone = input("Escreva seu telefone:")



'''
Impressão na tela.
'''

print("\n Olá, me chamo {nm}, tenho {idd} de idade e {alt} de altura. O número do meu CPF é {cpf} e minha residência fica na {end}. Para entrar em contato comigo, basta ligar para o número ({ddd}) {fn} que também é zap." .format(nm=nome, idd=idade, end=end, alt=altura, cpf=cpf, ddd=ddd, fn=fone))

