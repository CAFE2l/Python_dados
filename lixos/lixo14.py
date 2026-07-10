periodos = "1) 0-25 \n 2) 26-50 \n 3) 51-75 \n 76-100"
periodo = int(input("Digite um periodo para mostrar: "))

if periodo == 1:
    for i in range(1, 25 + 1):
        print(i)
elif periodo == 2:
    for i in range(26, 50 + 1):
        print(i)
elif periodo == 3:
    for i in range(51, 75 + 1):
        print(i)
elif periodo == 4:
    for i in range(76, 100 + 1):
        print(i)
