L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))


x = 0

while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x}. {p} Foi encontrado primeiro.")
        break
    elif L[x] == v:
        print(f"{v} achado na posição {x}. {v} Foi encontrado primeiro.")
        break
    x += 1
