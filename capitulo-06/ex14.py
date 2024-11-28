L = [1, 2, 3, 4, 5]
fim = 5

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)

# Como a lista já está ordenada, a condicional da linha 8 nunca é verdadeira e
# portanto não há troca de elementos.
