distancia = int(input("Digite a distância que quer percorrer em km: "))
preco = 0

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.5 * distancia

print(f"O preço da passagem é R${preco}")
