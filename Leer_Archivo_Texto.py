def Texto(direccion):
    archivo = open(direccion, 'r') 
    print("Indica la cantidad de palabras mas comunes")
    cant = int(input())+1
    contenido = archivo.read()
    contenido=contenido.lower()
    palabras=contenido.split() #Arreglo con todas las palabas
    #print("Cantidad total de palabras",len(palabras)) #Imprime la cantidad total de palabras
    diccionario_Palabras={} #Inicializa un diccionario vacio


    for pal in palabras: #Recorre la lista de todas las palabras
        for palabra in pal:
                palabra = palabra.lower().strip(".,?!-;:<>'")#Convierte a minusculs y evita los simbolos en los parametros
        try:
            diccionario_Palabras[pal]+=1 #Incrementa el contador de las palabras repetidas
        except KeyError:
            diccionario_Palabras[pal]=1 #Inicializa en 1 cuando encuentre una palabra nueva

    #Crea diccionarios vacios para almacenar las palabras repetidas y no repetidas
    dic_Repetidas={}
    dic_SinRepetir={}
    for c,v in diccionario_Palabras.items():
        if v>1:
            dic_Repetidas[c]=v #Si la palabra es repetida lo guarda en un nuevo diccionario para las palabras repetidas
        else:
            dic_SinRepetir[c]=v #Si la palabra no es repetida la almacena en un diccionario para las palabras sin repetir

    #Ordena por valores el diccionario
    import operator
    dic_Repetidas=sorted(dic_Repetidas.items(),key=operator.itemgetter(1))

    #Imprime los tama�os de los diccionarios de palabras con repeticion y posteriormente sin repeticion
    print("Cantidad de palabras repetidas ",len(dic_Repetidas))
    print("Cantidad de palabras sin repetir",len(dic_SinRepetir))

    #PALABRAS MAS COMUNES
    print("Listado de las ",cant-1, " palabras mas comunes")
    for i in range(1,cant):
        print(dic_Repetidas[-i])
        i=i+1

    archivo.close()

print("Indica el numero de opcion")
print("1) Texto en español")
print("2) Texto en ingles")
opcion=input()

if opcion == "1":
    Texto('El_Quijote.txt')
elif opcion == "2":
    Texto('Don_Quixote.txt')

