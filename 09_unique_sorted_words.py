def unique_sorted_words(entrada):
    return ", ".join(sorted(set(entrada.split(' '))))

print(unique_sorted_words('dog cat apple cat banana dog'))