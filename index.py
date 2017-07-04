#!/usr/bin/python
import sys, getopt
import unicodedata
words = {}

def main(argv):
   inputfile = ''
   outputfile = ''
   n = 30
   repetidas = 0
   sinrepetir= 0 
   try:
      opts, args = getopt.getopt(argv,"f:n:",["file=","number="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      if opt in ("-f", "--file"):
         inputfile = arg
      if opt in ("-n", "--number"):
         n = int(arg)

   print 'Input file is "',inputfile
   
   archivo = open(inputfile)
   
   for linea in archivo :
      linea = linea.replace(".", "") 
      linea = linea.replace(",", "") 
      linea = linea.replace(":", "")
      linea = linea.replace("-", "")
      linea = linea.replace(";", "")
      linea = linea.replace("?", "")
      linea = linea.replace("!", "")
      for word in linea.split() :
         repetidas += 1
         if words.has_key(word) == 0: 
            words[word] = 1
            sinrepetir += 1
         else :
            words[word] += 1
   imp = sorted(words.items(), key=lambda t: t[1], reverse=True)
   """print imp[1:n]"""
   i = 1
   for p in imp[0:n]:
      print i, p[0]
      i = i + 1
   print '# de palabras con repeticiones ', repetidas
   print '# de palabras sin repeticiones ', sinrepetir
if __name__ == "__main__":
   main(sys.argv[1:])
