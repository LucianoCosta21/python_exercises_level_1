def sort_words(texto):
    nomes_sorteado = ", ".join(sorted(texto.split(',')))
    return nomes_sorteado

print(sort_words('banana,apple,grape,orange'))
    