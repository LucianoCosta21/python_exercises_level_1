dic = {}
def generate_square_dict(numero):
    for indice in range(1, numero + 1):
        dic[indice] = indice ** 2
    return dic

print(generate_square_dict(8))