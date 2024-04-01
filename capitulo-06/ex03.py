lista1 = ["A", "B", "C"]
lista2 = ["C", "D", "E", "F", "G"]
lista3 = []

lista3.extend(lista1)

x = 0

while x < len(lista2):
    y = 0
    while y < len(lista3):
        if lista2[x] == lista3[y]:
            break
        elif y == (len(lista3) - 1):
            lista3.append(lista2[x])
            break
        else:
            y += 1

    x += 1

print(lista3)
