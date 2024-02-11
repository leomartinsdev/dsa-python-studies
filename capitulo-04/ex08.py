numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
operação = input(
    "Qual operação você deseja realizar: "
    "soma, subtração, multiplicação ou divisão? "
)

if operação == "soma":
    print(f"Resultado: {numero1 + numero2}")
elif operação == "subtração":
    print(f"Resultado: {numero1 - numero2}")
elif operação == "multiplicação":
    print(f"Resultado: {numero1 * numero2}")
else:
    print(f"Resultado: {numero1 / numero2}")
