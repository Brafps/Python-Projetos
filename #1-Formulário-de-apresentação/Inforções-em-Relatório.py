'''
 Faça um formulário que pergunte o nome, cpf, endereço, idade, altura e telefone.
 Depois imprima isso em um relatório organizado.
'''


nome = input("Escreva seu nome completo:")
cpf = input("Escreva seu cpf:")
end = input("Escreva seu endereço:")
idade = int(input("Escreva sua idade:"))
altura = float(input("Escreva sua altura:"))
ddd = input("Escreva seu DDD:")
fone = input("Escreva seu telefone:")


print("Olá, me chamo", nome, "tenho", idade, "de idade e", altura, "de altura.",
"O número do meu CPF é", cpf,
"e minha residência fica na "+end+". Para entrar em contato comigo, basta ligar para o número: ("+ddd+")", fone, "que também é zap")

