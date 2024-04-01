último = 10
# fila = list(range(1, último + 1))
fila = []

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    operação = input("Operação (F, A ou S): ")

    if operação == "A":
        atendido = fila.pop(0)
        print(f"Cliente {atendido} atendido!")
        # if len(fila) > 0:
        #     atendido = fila.pop(0)
        #     print(f"Cliente {atendido} atendido")
        # else:
        #     print("Fila vazia, ninguém para atender.")
    elif operação == "F":
        último += 1  # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida")


# RESPOSTA: ocorre um erro de "pop from empty list".
