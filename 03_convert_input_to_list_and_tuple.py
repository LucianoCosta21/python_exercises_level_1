def convert_input_to_list_and_tuple(lista_numeros):
    ##lista_final = ()
    numeros_para_lista = lista_numeros.split(",")
    ##lista_final = (numeros_para_lista , tuple(numeros_para_lista))
    return numeros_para_lista, tuple(numeros_para_lista)


print(convert_input_to_list_and_tuple("3,6,5,3,2,8"))
