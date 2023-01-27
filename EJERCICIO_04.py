def contador(texto):
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i]= 1
    return palabras

texto = "Todo es cuestión de actitud"
print(contador(texto))

