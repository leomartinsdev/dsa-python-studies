primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

decremento = primeiro_numero

while decremento >= segundo_numero:
    decremento -= segundo_numero

resto = decremento

print(f"Resto = {resto}")
