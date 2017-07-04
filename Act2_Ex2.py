import re as expresion
import operator
import argparse

parser=argparse.ArgumentParser(description='Procesador de textos')
parser.add_argument('arg_1', type=str, help="Texto para analizar")
parser.add_argument('-n',type=int, help="Palabras mas repetidas")
parser.add_argument("-l", action='store_true', help="Convertir el texto a minusculas")
args=parser.parse_args()

#total de palabras del texto
def contPalabras(texto):
    cont=0
    myfile=open(texto,'r')    
    texto=myfile.readlines()
    myfile.close()
    for row in texto:
        for word in row.split(' '):
            cont+=1
    return cont

#total de palabras sin repeticion
def contNoRepetidas(texto):
    repeticiones = {}
    coincidencias= expresion.findall(r'[\,a-z]{1,15}', texto)
    for word in coincidencias:
        cont_rep = repeticiones.get(word,0)
        repeticiones[word] = cont_rep + 1
    return repeticiones

if args.arg_1:
    total = contPalabras(args.arg_1)
    print '\n'+"El total de palabras con repeticion es de "+ str(total)
if args.l:
    #CONVIERTE EL ARCHIVO EN MINÚSCULAS PARA EVITAR TODAS LAS PALABRAS REPETIDAS
    myfile=open(args.arg_1)
    contenido=myfile.read().lower()
    myfile.close()
    rep = contNoRepetidas(contenido) #LISTA DE LAS PALABRAS NO REPETIDAS
    print "El total de palabras sin repeticion es "+ str(len(rep.items()))+'\n'
    #LISTA DE LAS PALABRAS NO REPETIDAS, ORDENADAS DE MAYOR A MENOR
    mas_rep=sorted(rep.items(), key=operator.itemgetter(1),reverse = True)
    #SI NO LE DA UN VALOR ESPECÍFICO A -n IMPRIME LAS 30 PALABRAS MAS REPETIDAS
    if args.n:
        indice=args.n 
    else:
        indice=30

    print 'Las ' +str(indice)+' palabras mas repetidas son....'
    i=0
    while i < indice:
        print str(i+1)+": "+str(mas_rep[i])
        i+=1
