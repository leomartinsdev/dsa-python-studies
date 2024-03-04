primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

quociente = 0
incremento = segundo

while incremento <= primeiro:
    quociente = quociente + 1
    incremento = incremento + segundo

print(quociente)
