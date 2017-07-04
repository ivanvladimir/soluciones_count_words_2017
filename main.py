
import re
import operator
import sys

dir_file = sys.argv[1]
n_words = int(sys.argv[3])
try:
	isLower = sys.argv[4]
except IndexError:
	isLower = ''

pattern_www = re.compile(r'www')
pattern = re.compile(r'\W*')
n_words_repeated = 0
dictionary = {}
list_common_words = []

file = open("common.txt", encoding="utf8")
for word_common in file:
	word_common = word_common.strip()
	list_common_words.append(word_common)

file = open(dir_file, encoding="utf8")
for line in file:
	line = line.strip()
	words = line.split()
	for word in words:
		if (isLower.lower()=="-l"):
			word = word.lower()
		if pattern.match(word):
			if pattern_www.match(word):
				pass
			else:
				word = re.sub(r'\W*', '', word)
		try:
			list_common_words.index(word)
		except ValueError:
			try:
				if(dictionary[word] == 1):
					n_words_repeated += 1
				dictionary[word] += 1
			except KeyError:
			   dictionary[word] = 1
file.close()

sort_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))

print ('Número de palabras encontradas ', len(dictionary))
print ('Número de palabras con repetición ', n_words_repeated)
print ('Número de palabras sin repetición ', len(dictionary)-n_words_repeated)
 
if (n_words<=0):
	pass
else:
	outfile = open('words.txt', 'w')
	count=1
	if (n_words>len(sort_dictionary)):
		n_words = len(sort_dictionary)
	print("Las {0} palabras más comunes son:".format(n_words))
	while (count<=n_words):
		index = len(sort_dictionary)-count
		tupla = sort_dictionary[index]
		count+=1
		string = "{0} : {1} \n".format(tupla[0],tupla[1])
		print (string, end="")
		outfile.write(string)
	outfile.close()
