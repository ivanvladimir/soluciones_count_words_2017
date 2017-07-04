#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import string

__author__ = "Ivan Fernando Galaviz Mendoza"


def leer_archivo(nombre_archivo, encoding='utf8'):
    with open(nombre_archivo, encoding=encoding) as f:
        contenido = f.readlines()
    contenido = [linea.strip() for linea in contenido]
    contenido = [linea.translate(str.maketrans('', '', string.punctuation)) for linea in contenido]
    return contenido

parser = argparse.ArgumentParser(description='Contar palabras de un texto.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('nombre_archivo', metavar='archivo', help='nombre del archivo de entrada.')
parser.add_argument('-l', '--lower', action='store_true', default=False,
                    help='convertir todas las palabras a minúsculas.', dest='conv_min')
parser.add_argument('-n', default=30, type=int, choices=range(1, 100),
                    help='cantidad deseada de palabras más comunes a mostrar.',
                    metavar='N', dest='cant_pal_comunes')

args = parser.parse_args()

palabras_ignoradas = leer_archivo('stopwords.txt', 'utf-8-sig')

lineas = leer_archivo(args.nombre_archivo, 'utf-8-sig')

if args.conv_min:
    lineas = [linea.lower() for linea in lineas]

repeticiones = {}

for linea in lineas:
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in palabras_ignoradas:
            if palabra in repeticiones:
                repeticiones[palabra] += 1
            else:
                repeticiones[palabra] = 1

print("Número de palabras con repeticiones: {0}".format(len([v for v in repeticiones.values()
                                                             if v > 1])))
print("Número de palabras sin repeticiones: {0}".format(len([v for v in repeticiones.values()
                                                             if v == 1])))

repeticiones_ordenadas = sorted(repeticiones.items(), key=lambda x: x[1], reverse=True)

cant_palabras = len(repeticiones_ordenadas)
if args.cant_pal_comunes <= cant_palabras:
    print("Las {0} palabras más comunes: ".format(args.cant_pal_comunes))
    for i in range(args.cant_pal_comunes):
        print(repeticiones_ordenadas[i])
else:
    print("No es posible mostrar {0} palabras, debido a que sólo hay {1}."
          .format(args.cant_pal_comunes, cant_palabras))
