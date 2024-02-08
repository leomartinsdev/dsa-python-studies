preço = int(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o desconto, sem o %: ")) / 100

print(f"O valor final é: R${preço * (1 - desconto)}")
