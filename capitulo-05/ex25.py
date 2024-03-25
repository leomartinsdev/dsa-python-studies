n = float(input("Digite um número: "))

b = 2
p = 0

while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada do número {n} é {p}")
