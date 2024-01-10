def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 2, 3, 3, 3, 4, 9, 6, 6, 9, 5]

lista = remove_repetidos(lista)
print(lista)