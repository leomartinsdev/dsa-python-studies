dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

print(
    f"O total em segundos é igual a "
    f"{segundos + (minutos * 60) + (horas * 3600) + (dias * 24 * 3600)}"
)
