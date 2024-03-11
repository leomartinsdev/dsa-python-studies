total_de_compras = 0

while True:
    preço = 0
    codigo_produto = int(input("Código do Produto: "))
    if codigo_produto == 1:
        preço = 0.50
    elif codigo_produto == 2:
        preço = 1.00
    elif codigo_produto == 3:
        preço = 4.00
    elif codigo_produto == 5:
        preço = 7.00
    elif codigo_produto == 9:
        preço = 8.00
    elif codigo_produto == 0:
        break
    else:
        print("Código Inválido")

    quantidade_comprada = float(input("Quantidade Comprada: "))
    total_de_compras += quantidade_comprada * preço

print(f"Total das Compras: {total_de_compras}")
