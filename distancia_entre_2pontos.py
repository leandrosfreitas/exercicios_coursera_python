import math

valor_x1 = float(input('Digite a coordenada (x) do primeiro ponto: '))
valor_y1 = float(input('Digite a coordenada (y) do primeiro ponto: '))
valor_x2 = float(input('Digite a coordenada (x) do segundo ponto: '))
valor_y2 = float(input('Digite a coordenada (y) do segundo ponto: '))

distancia = math.sqrt(((valor_x1 - valor_x2) ** 2) + ((valor_y1 - valor_y2) ** 2))
print(distancia)
if (distancia >= 10):
    print('longe')
else:
    print('perto')