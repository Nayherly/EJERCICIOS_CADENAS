def palabra(palabras):
    palabra_longitud=[]
    for p in palabras:
        palabra_longitud.append((len(p),p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]
palabras=['python','abril','carro','programación']
print(palabra(palabras))