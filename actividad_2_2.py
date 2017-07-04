

import re, string
import collections
import os

def act2(archivo, num):
    """función para imprimir el total de palabras"""

    Archivo_1=open(archivo, "r")
    """se abre el archivo del quijote y se guarda como una cadena"""
    texto= Archivo_1.read()
    Archivo_1.close()
    """se cierra el archivo"""

    if num==1:
         """si el parametro num=1 quiere decir que se necesita pasar todo el texto a minúscula antes de contar las palabras"""
         texto.lower()
    ''.join(e for e in texto if e.isalnum())
    """se eliminan los signos de puntuación de la cadena de texto"""

    palabras=texto.split()
    """se crea una lista con las palabras del texto"""
    palabras2=list(set(palabras))
    """se crea una lista con las palabras del texto donde no se repitan"""

    print ("numero de palabras con repetición ", len(palabras))
    """se imprime el total de palabras del texto"""
    print ("numero de palabras sin repetición ", len(palabras2))
    """se imprime el total de palabras sin repeticiones"""

    if num==2:
        """si el parametro num=2 quiere decir que el usuario va a ingresar el número de palabras más comunes que quiere ver"""
        n=int(input("¿Cuántas palabras desea ver?   "))
    else:
        n = 30

    lista_palabras=collections.Counter(palabras).most_common(n)
    """se guardan las n palabras más comunes"""
    t=0
    while t!=n:
        print (lista_palabras[t])
        t+=1
        """se imprimen las n palabras más comunes"""



print ("\t\tBienvenido al procesador de archivos\n")
print ("\n\n\n\t\tpresiona enter para empezar")
input()
os.system('clear')
"""pantalla de bienvenida"""

print ("PROCESANDO 'EL QUIJOTE' EN ESPAÑOL")
archivo="elquijote.txt"
act2(archivo, 0)
print ("\n\nPROCESANDO 'EL QUIJOTE' EN INGLÉS")
archivo="elquijoteingles.txt"
act2(archivo, 0)
i=0
while i!=3:
    i=int(input("\n\nopciones:\n1 contar palabras solo minúsculas\n2 contar n número de palabras más comunes\n3 salir\n"))
    if i==1:
        print ("PROCESANDO 'EL QUIJOTE' EN ESPAÑOL")
        archivo="elquijote.txt"
        act2(archivo, 1)
        print ("\n\nPROCESANDO 'EL QUIJOTE' EN INGLÉS")
        archivo="elquijoteingles.txt"
        act2(archivo, 1)
    elif i==2:
        print ("PROCESANDO 'EL QUIJOTE' EN ESPAÑOL")
        archivo="elquijote.txt"
        act2(archivo, 2)
        print ("\n\nPROCESANDO 'EL QUIJOTE' EN INGLÉS")
        archivo="elquijoteingles.txt"
        act2(archivo, 2)
    elif i==3:
        import sys
        sys.exit(0)
