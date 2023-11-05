num = int(input("Digite um número inteiro: "))
sep_num = str(num)
soma = 0

if num <= 10:
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("primo")
    else:
        print("não primo")
else:
    for i in range(len(sep_num)):
        soma += int(sep_num[i])
    if num % 2 == 0 or soma % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print("não primo")
    else:
        print("primo")