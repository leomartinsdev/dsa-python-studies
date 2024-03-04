primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

x = 1
res = 0

while x <= segundo:
    res = res + primeiro
    x = x + 1

print(res)
