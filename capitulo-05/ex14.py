contador = 0

while True:
    número = int(input("Número: "))
    contador += 1
    if número == 0:
        break

print(f"Números digitados: {contador}")
