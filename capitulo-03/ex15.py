cigarrosPorDia = int(input("Quantos cigarros você fuma por dia: "))
anosFumando = int(input("Quantos anos fumando: "))

cigarrosFumados = cigarrosPorDia * 365 * 4
vidaPerdidaEmMinutos = 10 * cigarrosFumados
print(f"Vida perdida em minutos: {vidaPerdidaEmMinutos}")

vidaPerdidaEmHoras = vidaPerdidaEmMinutos / 60
print(f"Vida perdida em horas: {vidaPerdidaEmHoras}")

vidaPerdidaEmDias = vidaPerdidaEmHoras / 24
print(f"Vida perdida em dias: {vidaPerdidaEmDias}")

print(
    (f"Você perdeu {vidaPerdidaEmDias} "
     "dias da sua vida devido ao hábito de fumar.")
)
