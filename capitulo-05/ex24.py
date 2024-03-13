while True:
    numero = 5  # int(input("Número de primos desejados: "))
    posicao = 1
    current_number = 3
    impar_atual = 1

    if numero == 1:
        print(f"{posicao}o número primo: 2")
        break
    else:
        print(f"{posicao}o número primo: 2")

        while posicao <= numero:
            if ((current_number % 2) == 0):
                current_number += 1
            else:
                while impar_atual < current_number:
                    if current_number % impar_atual == 0:
                        current_number += 1
                        break
                    else:
                        impar_atual += 2
        break

print(f"{posicao}o número primo: {current_number}")