coloniaA = 4  # 3%
coloniaB = 10
dias = 0

while coloniaA <= coloniaB:
    coloniaA *= 1.03
    coloniaB *= 1.015
    dias += 1
    print(f"Dia: {dias}")
    print(f"{coloniaA:.2f}")

print(
    f"Demorou {dias} dias para a coloniaA passar a coloniaB com um aumento de 3% chegou a {coloniaA:.2f}"
)
