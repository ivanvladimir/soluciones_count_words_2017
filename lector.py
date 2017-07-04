import argparse
analizador = argparse.ArgumentParser()
analizador.add_argument("archivo", help="Nombre de fichero a trabajar.",)
analizador.add_argument("-n", type=int, default=20, help="Total de palabras en el texto")
analizador.add_argument("-l",default=False, action='store_true',help="Convertir todas las letras en minuscula")
argumento = analizador.parse_args()

f = open(argumento.archivo,"r", encoding="utf8")
archivo = f.readlines()
contador = {} # diccionario para guardar ocurrencia de palabras
con=0
c=0
for linea in archivo:
    palabras = linea.split() #Hace separacion de la palabras por espacion es blanco
    for palabras in palabras:
        c+=1
        palabras = palabras.strip(",") # Elimina toda la puntuacion del texto
        if argumento.l is True:
            palabras = palabras.lower() #lower convirte el string en minisculas
        if palabras not in contador:
            contador[palabras] = 1
        else:
            contador[palabras] += 1


f.close() #Cierra el archivo


print('\n')
print('Total de palabras sin repeticion:', len(contador))
print('Total de palabras repetidas:', c)
print('Las',argumento.n,' Las palabras que más se repiten son:')
print('\n')
for palabras in sorted( contador, key = contador.get, reverse=True )[:argumento.n]:
    print('  ',palabras,':',contador[palabras],' total de veces encontrada')
