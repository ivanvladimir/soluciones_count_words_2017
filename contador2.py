#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import re
import string

def filtra_palabra(cadena, lower_tex):
	cadena = cadena.strip()
	palabra = re.sub('[%s%s¿¡«»]' % (string.punctuation, string.whitespace), '', cadena)
	if lower_tex == True:
		return str(palabra).lower()
	
	return palabra
	

def __main__():
	#n, lower_tex = redef_params()

	n = 30
	lower_tex = False
	ignore = False
	for x in sys.argv:
		if str(x) == "-l":
			lower_tex = True
		elif str(x) == "-n":
			n = int(sys.argv[sys.argv.index(x)+1])
		elif str(x) == "-i":
			ignore = True

	nombre_fichero = sys.argv[1]
	doc = open(nombre_fichero)
	lista_cadenas = list()

	for linea in doc:
		lista_cadenas += linea.strip().split(' ') 

	doc.close()
	
	palabra = str()
	dic_palabras = dict()
	for cadena in lista_cadenas:

		palabra = filtra_palabra(cadena, lower_tex)
		if dic_palabras.get(palabra) == None:
			dic_palabras[palabra] = 1
		else:
			dic_palabras[palabra] += 1
	
	can_palabras = 0
	for x in dic_palabras:
		#print("%s -> %d"  % (x,dic_palabras[x]))
		can_palabras += dic_palabras[x]
	
	lista_resultados = list(dic_palabras.items())
	lista_resultados.sort(key=lambda x: x[1])
	lista_resultados.reverse()
	lista_mas_repetidos = list()
	
	print("Palabras totales en el fichero >> %d" % len(dic_palabras))
	print("Palabras diferentes en el fichero >> %d" % can_palabras)
	print("Palabras más repetidas")

	# Lectura del fichero con las paralabras ignoradas
	doc = open("lista_ignorados.txt",'r')
	texto = doc.read()
	doc.close()

	# Generación de la lista de ignoradas
	lista = texto.split("\n")
	dicc_ignorados = dict()
	for x in lista:
		if dicc_ignorados.get(x) == None:
			dicc_ignorados[x] = 1

	i = 1

	if not(ignore):
		print("Sin ignorar las más comunes")
		for x in lista_resultados:
			if i <= n:
				print('%d.- %s -> %d' % (i,x[0],x[1]))
				i += 1
			else: break
	else:
		print("Ignorando las más comunes")
		for x in lista_resultados:
			if dicc_ignorados.get(x[0]) != 1:
				if i <= n:
					print('%d.- %s -> %d' % (i,x[0],x[1]))
					i += 1
				else: break
			else: pass
		
	


	# Sección de guardado de datos
	texto_resultado = str()
	for x in lista_resultados:
		texto_resultado += '%s -> %d\n' % (x[0],x[1])

	resultados = open('Resultados.txt','w')
	resultados.write(texto_resultado)
	resultados.close()

	
__main__()
