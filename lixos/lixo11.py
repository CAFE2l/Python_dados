numero = int(input("Digite um numero inteiro: "))
fatorial = 1


for i in range(1, numero + 1):
    fatorial *= i
    print(fatorial)


print(f"O fatorial de {numero} e {fatorial}")
