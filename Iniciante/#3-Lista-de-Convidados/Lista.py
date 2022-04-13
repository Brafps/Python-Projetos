

print("#-----------------------------#")
print("Programa controle de festas 1.0")
print("#-----------------------------#")

numero_de_convidados = int(input("Digite o número de pessoas que deseja convidar:"))

convidados = []

i=1

while i<= numero_de_convidados:
    nome_convidado = input("Digite o nome do convidado #"+str(i)+":")
    convidados.append(nome_convidado)
    i+=1

print("Lista de convidados")
print("\n Serão", numero_de_convidados, "convidados\n")

for convidado in convidados:
    print(convidado)
