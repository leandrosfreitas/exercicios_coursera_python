def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

print(MinMax([28, 32, 35, 29, 37, 24, 26, 32, 34, 24, 33, -5, 15, 40, 0, 11]))