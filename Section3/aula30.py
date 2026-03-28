"""
Apenas usando uma maneira melhor e mais legível de código
para o ambiente de trabalho
"""


RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
velocidade = input("Digite seu velocidade: ")
velocidade_real = int(velocidade)

vel_carro_pass_radar_1 = velocidade_real > RADAR_1


if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
