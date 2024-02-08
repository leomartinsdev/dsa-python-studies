kmPercorrido = float(input("Quantos km foram percorridos? "))
diasAlugados = int(input("Por quantos dias o carro foi alugado? "))

precoPagar = 0.15 * kmPercorrido + 60 * diasAlugados

print(f"O valor a ser pago é: R${precoPagar}")
