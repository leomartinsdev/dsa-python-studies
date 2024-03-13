while True:
    numero = int(input("Escolha um número: "))
    counter = 2

    if numero == 2:
        print("O número é primo!")
        break

    if (numero % counter) == 0:
        print("O número não é primo.")
        break

    counter += 1

    while counter <= numero:
        if counter == numero:
            print("O número é primo!")
            break
        elif (numero % counter) == 0:
            print("O número não é primo.")
            break
        else:
            counter += 1
    break
