import operator

def Minusculas(archivo,cantidad):
	libro={}
	totalPalabras=0
	SinRepe=0
	ConRepe=0

	lines=archivo.readlines()
	for line in lines:
		palabras=line.split()
		for p in palabras:
			p=p.lower()
			if libro.has_key(p):
				libro[p]=libro[p]+1
			else:
				libro[p]=1
		totalPalabras=totalPalabras+1
	for p in libro:
		if libro[p]==1:
			SinRepe+=1
		else:
			ConRepe+=1
	print "Total de Palabras: ",totalPalabras
	print "Con Repeticion: ",ConRepe
	print "Sin Repeticion: ",SinRepe

	libro = sorted(libro.items(), key=operator.itemgetter(1))
	libro.reverse()
	print libro[:cantidad]

def Contador(archivo,cantidad):


	libro={}
	totalPalabras=0
	SinRepe=0
	ConRepe=0
	lines=archivo.readlines()
	for line in lines:
		palabras=line.split()
		for p in palabras:
			if libro.has_key(p):
				libro[p]=libro[p]+1
			else:
				libro[p]=1
		totalPalabras=totalPalabras+1
	for p in libro:
		if libro[p]==1:
			SinRepe+=1
		else:
			ConRepe+=1
	print "Total de Palabras: ",totalPalabras
	print "Con Repeticion: ",ConRepe
	print "Sin Repeticion: ",SinRepe

	libro = sorted(libro.items(), key=operator.itemgetter(1))
	libro.reverse()
	print libro[:cantidad]

print "Favor de escoger una opcion"
print "Todo a minusculas: l"
print "Determinado numero de palabras: n"
Opcion1=raw_input("Opcion: ")

if Opcion1=='l':
			

	print "Actividad 2: "
	print "Ingles: 1"
	print "Espanol:2 "

	opcion=raw_input("Opcion: ")

	if opcion=='1':
		archivo=open("DonQuijoteIngles.txt")
		Minusculas(archivo,30)
	elif opcion=='2':
		archivo=open("DonQuijoteE.txt")
		Minusculas(archivo,30)

elif Opcion1=='n':

	print "Introduzca la cantidad de palabras a ver"
	cantidad=int(input("Palabra: "))

	print "Actividad 2: "
	print "Ingles: 1"
	print "Espanol:2 "

	opcion=raw_input("Opcion: ")

	if opcion=='1':
		archivo=open("DonQuijoteIngles.txt")
		Contador(archivo,cantidad)
	elif opcion=='2':
		archivo=open("DonQuijoteE.txt")
		Contador(archivo,cantidad)
else:
			
	print "Actividad 2: "
	print "Ingles: 1"
	print "Espanol:2 "

	opcion=raw_input("Opcion: ")

	if opcion=='1':
		archivo=open("DonQuijoteIngles.txt")
		Contador(archivo,30)
	elif opcion=='2':
		archivo=open("DonQuijoteE.txt")
		Contador(archivo,30)