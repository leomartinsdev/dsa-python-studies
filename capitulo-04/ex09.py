valor_casa = int(input("Valor da casa: "))
salário = int(input("Salário: "))
anos = int(input("Anos a pagar: "))

prestação_mensal = valor_casa / (anos * 12)

if prestação_mensal > (0.3 * salário):
    print("O valor da prestação mensal não pode ser superior à 30% do salário "
          f"Prestação mensal: {prestação_mensal} "
          f"| 30% do salário: {salário * 0.3}")
else:
    print("Empréstimo bancário aprovado. "
          f"Prestação mensal: {prestação_mensal}")
