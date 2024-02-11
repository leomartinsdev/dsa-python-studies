car_speed = int(input("Velocidade do carro: "))

if car_speed > 80:
    print(f"Você foi multado em R${5 * (car_speed - 80)}")
