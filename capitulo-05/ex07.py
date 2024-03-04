n = int(input("Tabuada de: "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))
x = inicio

while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
