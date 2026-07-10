numero = int(input("Digite um numero pra ver se e primo: "))

if numero < 2:
    print(f"O numnero {numero} nao e primo")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"O numero {numero} e primo")
    else:
        print(f"O numero {numero} nao e primo")
