salário = float(input("Salário: "))
base = 1250.00

if salário > base:
    salário = salário * 1.1
if salário < base:
    salário = salário * 1.15

print(f"Aumento: {salário}")
