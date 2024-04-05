L = []

for index in range(1, 21):
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)

x = 0
for number in L:
    print(L[x])
    x += 1

# Nem todo while pode ser substituído por for porque o for não pode rodar
# indefinidamente até que algo aconteça. A única maneira de fazer isso é com
# um loop infinito, que não pode ser parado de maneira alguma.
