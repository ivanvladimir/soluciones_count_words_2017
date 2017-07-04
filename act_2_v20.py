import argparse
import re
import operator

#ignorar todas las palabras
def ignora(recuperado, ignorar):
    listnew = []
    for w in recuperado:
        if w not in ignorar:
            listnew.append(w)
    return listnew

#recuperar archivos a ignorar   
def recupignore():
    arch = open("stopwords.txt","r")
    listaig = []
    for linea in arch:
        linea = linea.strip()
        bits = linea.split()
        listaig.extend(bits)
    return listaig

#recupera informacion
def recupinfo(archivo):
    print '\n\n\t\t\tTrabajando con: [', archivo, ']'
    arch = open(archivo,"r")
    listaw = []
    for linea in arch:
        linea = linea.strip()
        bits = linea.split()
        for w in bits:
            word = re.match("[a-zA-Z]+",w)
            if word != None:
                listaw.append(word.group())
    print '\t\t\tInformacion recuperada!'
    return listaw
    #print listaw


#Palabras con repeticiones
def palrept(lista):
	print 'Cantidad de palabras con repeticiones: ', len(lista)
#	print lista

#Palabras sin repeciones
def palsrept(lista):
	listaux = []
	for w in lista:
		if w not in listaux:
			listaux.append(w)
	print 'Cantidad de palabras sin repeticiones: ', len(listaux)
#	print listaux

#convertir palabras a minusculas
def tolower(lista):
	listalower = []
	for w in lista:
		listalower.append(w.lower())
	return listalower

#cuenta las palabras
def cuentaw(lista,n):
    print '\n\t\t Raking ', n, ' palabras mas comunes'
    cont = 1
    dic = {}
    for w in lista:
        if w not in dic:
            dic[w] = 1
        else:
            dic[w]= dic[w]+1
    dicaux = sorted(dic.items(), key=operator.itemgetter(1))
    dicaux.reverse()
    for k, v in dicaux:
        if cont == n+1:
            break
        else:
            print ("#{0} - {1}  [repeticiones: {2}]".format(cont, k, v))
            cont = cont + 1

#Procesado de argumentos de consola
p = argparse.ArgumentParser(
	prog= "Actividad 2 - Chatbos",
	epilog = "Jose Ramiro Ucan Bermon"
)
p.add_argument('-f','--file', help = 'Nombre del archivo a procesar', required=True)
p.add_argument('-l', action='store_true', help='Convertir todas las palabras a minusculas')
p.add_argument('-n',default=30, help='Cantidad de palabras comunes a regresar', action='store', dest='num')
p.add_argument('-i', action='store_true', help='Ignorar palabras dadas')
args = p.parse_args()


if args.l:
    print '\n\t\tConversion a minusculas'
    words = recupinfo(args.file)
    if args.i:
        print 'Ignorando palabras...'
        wordsig = recupignore()
        words = ignora(words,wordsig)
    tolow = tolower(words)
    palrept(tolow)
    palsrept(tolow)
    cuentaw(tolow,int(args.num))
else:
    words = recupinfo(args.file)
    if args.i:
        print 'Ignorando palabras...'
        wordsig = recupignore()
        words = ignora(words,wordsig)
    palrept(words)
    palsrept(words)
    cuentaw(words,int(args.num))
