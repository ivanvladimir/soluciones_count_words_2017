import operator
import sys

option = None
numb_ret_words = 30
file = open(sys.argv[1], 'r+')
bad_words = open('stopwords.txt', 'r+', encoding = 'utf8')
#"""
if len(sys.argv) == 1:
    numb_ret_words = 30
if len(sys.argv) == 3 or sys.argv[2] == 'l':
    option = sys.argv[2]
if len(sys.argv) == 3 or sys.argv[2] == 'n':
    numb_ret_words = sys.argv[3]
if len(sys.argv) == 5:
    option = sys.argv[2]
    numb_ret_words = sys.argv[4]
#"""


if option == 'l':
    lines = [line.lower() for line in file]
    with open(str(sys.argv[1]), 'w', encoding = 'utf8   ') as out:
        out.writelines(lines)

file = open(sys.argv[1], 'r', encoding = 'utf8')
lines = file.readlines()
lines_bad_words = bad_words.readlines()
words = {}
bad_words_dict = {}

for line_bad_words in lines_bad_words:
    for g in line_bad_words.split( ):
        if g not in bad_words_dict.keys():
            bad_words_dict [g] = 1

for line in lines:
    for x in line.split( ):
        
        if x.startswith('-'):
            x = x[1:]
        if x.endswith(','):
            x = x[:len(x)-1]
        if (x.endswith('-')):
            x = x[:len(x)-1]
        if(x.endswith(',-')):
            x = x[:len(x)-2]
        if x in words.keys():
            value = words.get(x)
            value += 1
            words[x] = value
        if x not in words.keys() and x not in bad_words_dict.keys():
            words[x] = 1    
number_words = 0 

for x in words.keys():
    number_words += words.get(x)
words = sorted(words.items(), key=operator.itemgetter(1))
words.reverse()

#print(words)
print("Numero de palabras sin repeticiones  " + str(len(words)) + "\n"\
    + "Numeros de palabras con repeticiones " + str(number_words)\
    + "\n" + " Las " + str(numb_ret_words) + " palabras mas comunes ")
for word in range(int(numb_ret_words)):
    print(list(words)[word])