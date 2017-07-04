import argparse
analizador = argparse.ArgumentParser()
analizador.add_argument("archivo", help="Indica el nombre del fichero a trabajar.",)
analizador.add_argument("-n", type=int, default=30, help="Numero de palabras mas aparecidas")
analizador.add_argument("-l",default=False, action='store_true',help="Convertir todas las letras en minuscula")
argumento = analizador.parse_args()

f = open(argumento.archivo,"r", encoding="utf8")


archivo = f.readlines()
contador = {} # diccionario para guardar ocurrencia de palabras
con=0
c=0
for linea in archivo:
    palabras = linea.split() # separar lÃ­nea en palabras, por espacio en blanco
    for palabra in palabras:
        c+=1
        palabra = palabra.strip(".,") # quitar puntuaciÃ³n
        if argumento.l is True:
            palabra = palabra.lower()
        if palabra not in contador:
            contador[palabra] = 1
        else:
            contador[palabra] += 1

# Cerrar archivo al finalizar
f.close()


print('\n')
print('palabras sin repeticiones:', len(contador))
print('palabras con repeticiones:', c)
print('Las',argumento.n,'  palabras mas comunes son:')
print('\n')
for palabra in sorted( contador, key = contador.get, reverse=True )[:argumento.n]:
    print('  ',palabra,':',contador[palabra],'veces que se encuentran')
