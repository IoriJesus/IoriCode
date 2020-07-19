#Author Montes Martínez Jesús Iori
import sys
import time
import random
from tkinter import*
from datetime import datetime
sys.setrecursionlimit(1000)

file = open("Data.txt", "a")

time = str(datetime.now())
expresiones = []

file.write('Test at '+time+'\n')
print ("Generador de cadenas de la expresión: (0 U 10)*(e U 1)")	
file.write("Generador de cadenas de la expresión: (0 U 10)*(e U 1)")

for i in range(0,10):
        
	print(i+1,".-")
	file.write("\n"+str(i+1)+".-")
	expresiones.append("")

	ck = random.choice(["", "n"])
	print ("ck=",ck)
	file.write("\n"+"ck ="+ck)

	if ck == "n":
                
		n = random.randint(1, 10)
		print("n:",n)
		file.write("\n"+"n:"+str(n))
		
		for j in range(0,n):
			a1 = random.choice(["0", "10"])
			print("a1=",a1)
			file.write("\n"+"a1="+a1)
			expresiones[i] = expresiones[i]+a1



	print ("Expresion antes de la multiplicacion:",expresiones[i])
	file.write("\n"+"Expresion antes de la multiplicacion:"+expresiones[i])

	a2 = random.choice(["", "1"])
	print("a2="+a2)
	file.write("\n"+"a2="+a2)


	if(a2=="1"):
		print("Hay 1 al final, se suma")
		file.write("\n"+"Hay 1 al final, se suma")
		expresiones[i] = expresiones[i]+a2 	

	print (expresiones[i], "\n")
	file.write("\n"+expresiones[i]+ "\n")

print (expresiones)
file.write("\n"+str(expresiones)+"\n")
file.close()
