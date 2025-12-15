def find_numbers(a,b):
    lista = []
    for numeros in range(a,b + 1):
        divisivel_por_7 = numeros % 7
        multiplo_de_5 = numeros % 5
        if divisivel_por_7 == 0 and multiplo_de_5 != 0:
            lista.append(str(numeros))
        
    return ','.join(lista)
   

print(find_numbers(100,200))