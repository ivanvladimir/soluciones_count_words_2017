from collections import Counter
import argparse

p = argparse.ArgumentParser("Contador de palabras")
p.add_argument("Archivo",default=None,action="store", help="Archivo Uno")
p.add_argument("Lower",default=None,action="store", help="Minusculas")
p.add_argument("num_palabras",default=None,action="store", help="Numero de palabras")



opts=p.parse_args()
opts=vars(opts)
archivo=open(opts['Archivo'],'r')

lista_palabras=[]
for linea in archivo:
	line=linea.strip()
	bits=line.split()
	lista_palabras+=bits

	
	
if opts['Lower']== 'l':
		for i in range(0,len(lista_palabras),1):
			lista_palabras[i]=str.lower(lista_palabras[i])
			
	
b=sorted(lista_palabras)
print "Numero de palabras con repedition: " + str(len(b))

palabras= Counter (b)
palabras=dict(palabras)
ocurrencia=palabras.values()

print "Numero de palabras sin repedition: " + str(len(ocurrencia))

sin_repe=0
con_repe=0

for i in ocurrencia:

	if i==1:
		sin_repe+=1
	else:
		con_repe+=1

valores=[(v,k) for k, v in palabras.items()]
valores=sorted(valores, reverse=True)


print "LAS 30 PALABRAS COMUNES"
for i in range(0, int(opts['num_palabras']), 1):
	print valores[i]
