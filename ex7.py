distancia = float(input("Digite a distância percorrida (km): "))
combustivel = float(input("Digite a quantidade de combustível consumido (litros): "))


if combustivel == 0 or distancia == 0:
        print("O consumo não pode ser calculado, pois a quantidade de combustível ou a distância percorrida é zero.")
else:       
        consumo = distancia / combustivel
                
        if consumo < 8:
                        mensagem = "Consumo alto! Melhor trocar de carro."
        elif 8 <= consumo <= 12:
                        mensagem = "Consumo moderado."
        else:
                        mensagem = "Consumo eficiente!"
                
        print(f"O consumo foi de {consumo} km/l. {mensagem}")
