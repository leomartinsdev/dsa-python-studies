último_fila1 = 10
último_fila2 = 10
fila1 = list(range(1, último_fila1 + 1))
fila2 = list(range(1, último_fila2 + 1))

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e")
    print(f"{len(fila2)} clientes na fila 2.")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("ou G para adicionar um cliente ao fim da fila 2.")
    print("\nDigite A para realizar o atendimento na fila 1 ou B para")
    print("atendimento na fila 2. S para sair.")

    operação = list(input("Operação (F, G, A, B ou S): "))

    index = 0

    while index < len(operação):
        if operação[index] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia, ninguém para atender.")
            index += 1
        elif operação[index] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia, ninguém para atender.")
            index += 1
        elif operação[index] == "F":
            último_fila1 += 1  # Incrementa o ticket do novo cliente
            fila1.append(último_fila1)
            index += 1
        elif operação[index] == "G":
            último_fila2 += 1  # Incrementa o ticket do novo cliente
            fila2.append(último_fila2)
            index += 1
        elif operação[index] == "S":
            break
        else:
            print("Operação inválida")
