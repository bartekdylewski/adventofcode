def funkcja(lista):
    lista.sort() # [2000,2001,2003,...]
    rok = []
    ilosc = []
    for element in lista:
        if element in rok:
            id = rok.index(element)
            ilosc[id] += 1
        else:
            rok.append(element)
            ilosc.append(1)
    wynik = list(zip(rok,ilosc))
    return wynik
    
print(funkcja([2000,2001,2004,2001,2001,2000,2005]))