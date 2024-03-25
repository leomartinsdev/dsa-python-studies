número = input("Número: ")

i = 0
last = len(número) - 1

while last > i and número[i] == número[last]:
    i += 1
    last -= 1

if número[i] == número[last]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
