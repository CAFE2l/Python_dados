temperaturas = []
while True:
    temperatura = float(input("Digite uma temperatura (-273 para pausar programa): "))

    if temperatura != -273:
        temperaturas.append(temperatura)

    elif temperatura == -273:
        break


media_temperaturas = sum(temperaturas) / len(temperaturas)


print(
    f"Temperaturas digitadas{temperaturas} e a media das temperaturas inseridas foi de {media_temperaturas}"
)
