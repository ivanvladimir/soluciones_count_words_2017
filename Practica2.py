#!/usr/bin/python
# coding:utf-8
import collections
import re
import argparse

parser = argparse.ArgumentParser(description='Actividad 2')

parser.add_argument("-n", help="Regresa N palabras", type=int, dest='N')
parser.add_argument("-l", help="Convierte todas las palabras a minúsculas",action="store_true",
					 dest='L')
parser.add_argument("-a", help="Solicita el libro para trabajar", type=str, dest='x')

args = parser.parse_args()
N = args.N
libro = args.x

if args.L:

	words = re.findall(r'\w+', open(libro).read().lower())
	count = dict(collections.Counter(words))
	i=0
	for k,v in count.iteritems():
		if v == 1:
			i+=1
		else:
			i+=1
	print ""
	print str(i)+" palabras sin repetir"

	words = re.findall(r'\w+', open(libro).read().lower())
	count = sum(dict(collections.Counter(words)).values())
	print ""
	print str(count)+" palabras con repeticiones de acuerdo a diccionario"

	words = re.findall(r'\w+', open(libro).read().lower())
	count = collections.Counter(words).most_common(30)
	print ""
	print "Las 30 palabras más comunes: "
	print count
	if args.N:
		if N > 0:
			words = re.findall(r'\w+', open(libro).read())
			count = collections.Counter(words).most_common(N)
			print ""
			print str(N)+" palabra(s) comunes"
			print count
	archivo=open(libro,'r')

	i=0
	for linea in archivo:
    		pal=len(linea.split())
    		i+=pal
	print ""
	print str(i)+" palabras con repeticiones de acuerdo a word"

	archivo.close()
else:
	if args.N:
		if N > 0:
			words = re.findall(r'\w+', open(libro).read())
			count = collections.Counter(words).most_common(N)
			print ""
			print str(N)+" palabra(s) comunes"
			print count


	words = re.findall(r'\w+', open(libro).read().lower())
	count = dict(collections.Counter(words))
	i=0
	for k,v in count.iteritems():
		if v == 1:
			i+=1
		else:
			i+=1
	print ""
	print str(i)+" palabras sin repetir"

	archivo=open(libro,'r')

	i=0
	for linea in archivo:
    		pal=len(linea.split())
    		i+=pal
	print ""
	print str(i)+" palabras con repeticiones de acuerdo a word"

	archivo.close()

	words = re.findall(r'\w+', open(libro).read())
	count = sum(dict(collections.Counter(words)).values())
	print ""
	print str(count)+" palabras con repeticiones de acuerdo a diccionario"

	words = re.findall(r'\w+', open(libro).read())
	count = collections.Counter(words).most_common(30)
	print ""
	print "Las 30 palabras más comunes: "
	print count




