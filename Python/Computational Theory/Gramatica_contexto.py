import random
import time
from datetime import datetime

rule = 0
String = ["p"]
time = str(datetime.now())
file = open("Data.txt","a")


def add(state, rule):
        file .write("(" +str(rule)+ ") .- " + str(String) + "\n")

def build(length):
	global String
	global rule

	parte_1 = [1, 2, 3]									
	parte_2 = [4, 5]	
					

	for i in range(1, length+1):

		print("valor de i: " + str(i))
		aux = len(String)

		if i == length:
			
			x = random.choice(parte_1)

			if x == 1:
				posicion = String.index("p")
				String[posicion] = "E"
				add(state, 1)
				print(String)
				String.remove("E")
				print(String)
				state=1
				rule = x
				add(state, rule)
				
			else:
				if x == 2:
					posicion = String.index("p")
					String[posicion] = 0
					print(String)
					state=1
					rule = x
					add(state, rule)

				else:
					if x == 3:
						posicion = String.index("p")
						String[posicion] = 1
						print(String)
						state=1
						rule = x
						add(state, rule)
				

		else:
			if i != length:
				y = random.choice(parte_2)					

				if y == 4:
					String.append(0)
					String.append(0)
					posicion = String.index("p")
					if i == 1:
						String[posicion], String[posicion+1] = String[posicion+1], String[posicion]
					else:
						for x in range(aux+1):
							String[x], String[-2] = String[-2], String[x]

					print(String)
					state=0
					rule = y
					add(state, rule)

				else:
					String.append(1)
					String.append(1)
					posicion = String.index("p")
					if i == 1:
						String[posicion], String[posicion+1] = String[posicion+1], String[posicion]
					else:
						for x in range(aux+1):
							String[x], String[-2] = String[-2], String[x]

					print(String)
					state=0
					rule = y
					add(state, rule)
					

length_input = input('Ingrese la longitud de la cadena  o de click  en Intro para generar una cadena automatica: ')
file.write('Test at '+time+'\n')

if length_input  == '':
        length = random.randrange(20)
        print(length)
        build(length)
else:
    length = int(length_input)
    build(length)

file.close()
