import math
def calculate_q_values(entrada):
    C = 50
    H = 30
    valores = []
    listA_numeros = entrada.split(",")
    for numeros in listA_numeros:
        Q = round(math.sqrt((2 * C * int(numeros) / H)))
        valores.append(str(Q))       
    return  valores

print(calculate_q_values("100,150,180"))