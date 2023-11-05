seg_converter = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = seg_converter // 86400
horas = (seg_converter % 86400) // 3600
minutos = ((seg_converter % 86400) % 3600) // 60
segundos = ((seg_converter % 86400) % 3600) % 60

print(f'{int(dias)} dias, {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos.')