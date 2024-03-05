deposito_inicial = int(input("Depósito Inicial: "))
juros = float(input("Taxa de Juros: "))
montante = deposito_inicial
x = 1

# Vou supor que seja juros sobre juros. Então o deposito inicial é atualizado
# pelo juros e o próximo juros é sobre o montante total

while x <= 24:
    montante = montante + (montante * juros)
    x = x + 1

print(f"Ganho com Juros = {montante - deposito_inicial}")
