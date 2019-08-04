def remove_repetidos(lista):
    aux=lista[:]
    x=len(lista)
    novo=[]
    for item in lista:
        if item not in novo:
            novo.append(item)
    
    for i in range(len(novo)):
        lista[i]=novo[i]

    diferença=len(lista)-len(novo)+1
    for j in range(1,diferença):
        del lista[-1]

    lista.sort()
            
    return lista
