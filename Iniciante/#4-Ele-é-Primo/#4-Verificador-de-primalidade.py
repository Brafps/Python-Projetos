
print("Digite um número inteiro positivo e irei verificar se o número é ou não um número primo.")

num = int(input("\n Digite o número que deseja testar: "))
num_div = 0

for i in range(1, num +1):
    if (num % i == 0):
        num_div = num_div +1

if num_div == 2:
    print("O número %d é primo" %num)
else:
    print("O número %d não é primo" %num)    