cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "pretoebranco": "\033[7;30m",
}

fundo = {
    "branco": "\033[m",
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m",
    "azul": "\033[44m",
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m",
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
}
frase = "numeros dentro de um periodo"
print(
    f"{cores['amarelo']}{estilos['negrito']}{'==' * 10 + '='}{cores['verde']}FATORIAL{cores['limpa']}{cores['amarelo']}{estilos['negrito']}{'==' * 11}{cores['limpa']}"
)
print(
    f"{cores['vermelho']}{estilos['italico']}{estilos['negrito']}{frase.center(50)}{estilos['reset']}"
)
print(f"{cores['amarelo']}{estilos['negrito']}{'===' * 17}{cores['limpa']}")
num1 = int(input("Digite 1 numero: "))
num2 = int(input("Digite o segundo numero: "))


menor, maior = min(num1, num2), max(num1, num2)

if menor != maior:
    print(f"Os numeros que estao no periodo de {menor} e {maior} sao: ")
    for n in range(menor + 1, maior):
        print(n)

else:
    print("Os numeros sao iguais, nao ha periodos")
