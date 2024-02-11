consumo_kWh = int(input("Quantidade de kWh consumida: "))
tipo_instalacao = input("Tipo de instalação: R para residências, "
                        "I para indústrias e C para comércios: ")

preço = 0

if tipo_instalacao == "R":
    if consumo_kWh < 500:
        preço = 0.4
        print("Preço para residências com consumo abaixo de 500 kWh: R$0.40")
    else:
        preço = 0.65
        print("Preço para residências com consumo acima de 500 kWh: R$0.65")
elif tipo_instalacao == "C":
    if consumo_kWh < 1000:
        preço = 0.55
        print("Preço para comércios com consumo abaixo de 1000 kWh: R$0.55")
    else:
        preço = 0.60
        print("Preço para comércios com consumo acima de 1000 kWh: R$0.60")
else:
    if consumo_kWh < 5000:
        preço = 0.55
        print("Preço para indústrias com consumo abaixo de 5000 kWh: R$0.55")
    else:
        preço = 0.6
        print("Preço para indústrias com consumo acima de 5000 kWh: R$0.60")
