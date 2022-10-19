def remove_elements_from_list(lista,listb):
    for i in listb:
        lista.remove(i)
    return lista

lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
print(f"from {lista} remove {listb},结果为：",remove_elements_from_list(lista,listb))
