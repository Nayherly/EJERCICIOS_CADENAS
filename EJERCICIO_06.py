def reemplazar(sub_cadena):
    print(sub_cadena)
    cadena_remove =str(input("Ingrese la subcadena que va reemplazar: "))
    for i in range(len(sub_cadena)):
        if sub_cadena[i] == cadena_remove:
            new_subCadena = str(input("Ingrese nueva subcadena: "))
            sub_cadena[i]= new_subCadena
       

cadena = "Hola mi nombre es Nayherly"
sub_cadena = cadena.split()

print(reemplazar(sub_cadena))
