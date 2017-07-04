print "¿Cual es el nombre del texto que desea analizar (con extencion.txt)?"
texto = raw_input()+".txt"

print "¿Deseas convertir todas las palabras a minusculas? y = si"
min = raw_input()

print "¿Cual es el numero de palabras mas comunes que desea obtener?"
comunes = input()

archivo = open(texto,'r')
contenido = archivo.readlines()
archivo.close()

contador = 1
lista1 = []
lista2 = []
lista3 = []

for renglon in contenido:

    for palabra in renglon.split(' '):

        palabra = palabra.strip(')')
        palabra = palabra.strip(',')
        palabra = palabra.strip('.')
        palabra = palabra.strip('?')
        palabra = palabra.strip(';')
        palabra = palabra.strip(':')
        palabra = palabra.strip('"')
        palabra = palabra.strip('!')
        palabra = palabra.strip(' ')

        print contador, "Analizando la Palabra: ",palabra

        if  len(palabra) == 0:
            pass

        else:
            if min == "y":
                repeticion = 0
                lista1.append(palabra.lower())
                contador += 1
            else:
                repeticion = 0
                lista1.append(palabra)
                contador += 1

            for i in lista2:
                if palabra == i:
                    repeticion += 1

            if repeticion == 0:
                if min == "y":
                    lista2.append(palabra.lower())
                else:
                    lista2.append(palabra)

for i in lista2:
    frecuencia = lista1.count(i)
    lista3.append(frecuencia)
    print str(frecuencia) + ': ',i

n=0
aux = 0
valor = 0
v=0

print "Numero de palabras (con repeticiones) = ", len(lista1)
print "Numero de palabras (sin repeticiones) = ", len(lista2)

while n < comunes:
    for k in lista3:
        if lista3[v] > valor:
            aux = v
            valor = lista3[v]
        v += 1
    n+=1
    lista3[aux] = 0
    print "Numero "+ str(n)+" con mayor frecuencia",lista2[aux]
    aux=0
    valor=0
    v=0