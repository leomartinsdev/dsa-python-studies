estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas:\n")

while True:
    produto = input("Digite o nome do produto (0 para sair): ")
    if produto == "0":
        print("Saindo do sistema...")
        break
    elif produto not in estoque:
        print("Produto não encontrado!")
        continue
    quantidade = int(input("Digite a quantidade: "))
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto}: {quantidade} x {preço} = {custo}")
    estoque[produto][0] -= quantidade
    total += custo
print(f" Custo total: {total}:\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]}:\n")
