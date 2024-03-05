divida_inicial = int(input("Dívida Inicial: "))
juros_mensal = float(input("Juros mensal: "))
pagamento_mensal = int(input("Pagamento mensal: "))

meses = 0
total_juros_pago = 0
total_pago = 0

while divida_inicial > 0:
    meses += 1
    juros = divida_inicial * (juros_mensal / 100)
    divida_inicial += juros
    divida_inicial -= pagamento_mensal

    total_pago = pagamento_mensal

total_juros_pago = total_pago - divida_inicial

print(
    f"Número de meses para pagar: {meses}"
    f"| Total pago: R${total_pago} |"
    f"Total de Juros Pago: R${total_juros_pago}"
)
