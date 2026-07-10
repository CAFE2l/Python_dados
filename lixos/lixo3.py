# notas de 0 a 5 sobre os servicos oferecidos
# verificar se o servico for valido ou naoa

notas_permitidas = [0, 1, 2, 3, 4, 5]
notas = []
usuario = 0
for i in range(15):
    nota = int(input("digite uma nota sobre nossos servicos de 0 - 5: "))
    while nota not in notas_permitidas:
        print(f"nota invalida tente novamente")
        nota = int(input("Digite novamente (0 - 5): "))
    notas.append(nota)
print(notas)
