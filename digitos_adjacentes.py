num = input("Digite um número inteiro: ")
digitos = [int(d) for d in num]
repeated = ""

for i in range(len(digitos)-1):
    if digitos[i] == digitos[i+1]:
        repeated = True
        if repeated == True:
            break
    else:
        repeated = False
if repeated == True:
    print("sim")
else:
    print("não")
