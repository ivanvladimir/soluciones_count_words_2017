from collections import Counter
abrir=raw_input('Nombre de archivo: ')
hlower=raw_input('Convertir a minusculas: y/n ')
numero=int(raw_input('Numero de palabras: '))
archivo=open(abrir)
words = [word for line in archivo for word in line.split()]
if hlower == 'y':
	words = [x.lower() for x in words]
print "Total de palabras: ", len(words)
print "total de palabras sin repetir: ",len(dict.fromkeys(words).keys())
c = Counter(words)
for word, count in c.most_common(numero):
	print word, count
archivo.close()