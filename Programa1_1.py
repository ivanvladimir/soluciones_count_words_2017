archivo=open("C:/Users/AlAn-/Desktop/texto2.txt","r")
cadena=archivo.read() 
texto=cadena.split()
norep=set(texto)
print("Total de palabras: ",len(texto))  #Palabras con repetición
print("Total de palabras diferentes: ",len(norep)) #Palabras sin repetición
frecuencia=[texto.count(i) for i in norep] #frecuencia
numfre=list(zip(norep,frecuencia))  #Lista con frecuencia y palabras
dic=dict(numfre) #Se convierte en diccionario
aux=[(dic[key],key) for key in dic] #Se crea una lista nueva para acomodar los valores
aux.sort()
aux.reverse()
i=0
print("Las 30 palabras más comunes son:")
print("PALABRA/FRECUENCIA")
for val0,val1 in aux:
    print("{1} {0}".format(val0,val1)) #Template para cadena
    i+=1
    if i == 30: #El ciclo se detiene hasta las 30 palabras más usadas
        break
