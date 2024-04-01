último = 10
fila = list(range(1, último + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    operação = list(input("Operação (F, A, S): "))

    index = 0

    while index < len(operação):
        if operação[index] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia, ninguém para atender.")
            index += 1
        elif operação[index] == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
            index += 1
        elif operação[index] == "S":
            break
        else:
            print("Operação inválida")
