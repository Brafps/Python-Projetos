

print("---------------")
print("Serviço Militar")
print("---------------")


idade = int(input("Escreva sua idade:"))
massa = float(input("Escreva sua massa:"))
altura = float(input("Escreva sua altura:"))


if idade >= 18 and massa >= 60 and altura >= 1.70:
    print("Você está apto a servir o exercito!")

else:
    print("Você não está apto.")