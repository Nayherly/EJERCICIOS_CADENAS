def longitud(sub_cadena):
    for i in range(len(sub_cadena)):
        sc = str(sub_cadena[i])
        if sc.isdecimal() is True:
            print('La longitud de la subcadena {} es: '.format(sc), len(sc))


cadena = str(input('Ingrese una cadena: '))
subcadenas = cadena.split(' ')
print(subcadenas)
print(len(subcadenas))