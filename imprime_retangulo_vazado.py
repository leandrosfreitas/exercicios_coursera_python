largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
count = altura - 2

if altura <= 2:
    while altura > 0:
        print(largura * '#')
        altura -= 1
if altura > 2:
    print('#' * largura)
    while altura > 2:
        print('#', ' ' * (largura - 4), '#')
        altura -= 1
        count -1
    print('#' * largura)