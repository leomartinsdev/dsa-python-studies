while True:
    option = int(
        input(
            "Opções: \n 1 - Adição \n 2 - Subtração \n 3 - Divisão \n"
            " 4 - Multiplicação \n 5 - Sair \n Opção escolhida: "
        )
    )

    if option == 5:
        break
    elif 1 <= option < 5:
        n = int(input("Tabuada de: "))
        x = 1

        while x <= 10:
            if option == 1:
                print(f"{x} + {n} = { x + n }")
            elif option == 2:
                print(f"{x} - {n} = { x - n }")
            elif option == 1:
                print(f"{x} / {n} { float(x / n) }")
            elif option == 1:
                print(f"{x} x {n} = { x * n }")
            x += 1
