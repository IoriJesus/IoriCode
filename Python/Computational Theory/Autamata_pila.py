import time
import random
from random import randint
from datetime import datetime

cadena = []
pila = ['Z0']
bandera = True
time = str(datetime.now())
file = open("Data.txt", "a")

def Evaluar():
	global pila
	global bandera

	aux = cadena[:]

	file.write(str(cadena) + " <--- [q] ---> " + str(pila) + "\n")
	a = 0

	for i in cadena:
		print(i)
		
		if (i == '0'):
			pila.append('X')
			aux.pop(0)
			print(f"(q,0, {pila[-1]}" + "}" + " = {(q, X" + pila[-1] + ")}")
			file.write(str(aux) + " <--- [q] ---> " + str(pila) + "\n")
		else:
                        
			if(i == '1' and len(pila) != 1):	
				print("(p,1,X) = {(p, E)}")
				pila.pop();
				aux.pop();
				file.write(str(aux) + " <--- [p] --->" + str(pila) + "\n")
			else:
				bandera = False
				print("esta cadena no es aceptada.")
				break
		a = 1
	file.close();

cad = input('Ingrese la cadena a evaluar o de click  en Intro para generar una cadena automatica: ')
file.write('Test at '+time+'\n')

if cad == '':
    rand = random.randrange(10000)
    cad = str(bin(rand)[2:])
    print(cad)

for letra in cad:
	cadena += letra

print(pila)

Evaluar()

if(bandera == True):
	file = open("Data.txt", "a")
	lol = []											
	print("(p,E,Z0) = {(f, z0)}")
	file.write(str(lol) + " <--- [F] --->" + str(pila) + "\n")
	file.close()


