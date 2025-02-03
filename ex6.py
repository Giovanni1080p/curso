horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
x = horas * 3600 + minutos * 60 + segundos

print(f"O total em segundos é: {x}")