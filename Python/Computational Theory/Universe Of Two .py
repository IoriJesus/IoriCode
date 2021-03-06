#Author Montes Martínez Jesús Iori
import sys
import random

file = open('Universe.txt','w')
file20 = open('Universe20.txt','w')
file60 = open('Universe60.txt','w')
file100 = open('Universe100.txt','w')

def verify_date():
    number = input('write one number:')
    
    if number == '':
            number=random.randrange(27)
            print(number)
        
    try:
    	number = int(number)
    	if number > 1:
    	    file.write('{')
    	    return number
    	else:
    	    if number == 1:
    	        print('{1,0,ε}')
    	        file.write('{1,0,ε}')
    	        sys.exit(0)
    	        
    	    if number == 0:
    	        print('{ε}')
    	        file.write('{ε}')
    	        sys.exit(0)
    	        
    	    if number < 0:
    	        print('This program don´t accepted numbers smaller than 0')
    	        sys.exit(1)
    except ValueError:
        print("datas don´t valid")
        sys.exit(1)

number_universe=verify_date()
for i in range(0,number_universe): 
	combinations = 2 ** number_universe 
	auxpot = number_universe
	spacetext=0

	while combinations > 0:

		if combinations != 2**number_universe:

			file.write(str(bin(combinations)[2:number_universe+2]).zfill(number_universe))
			file.write (",")
			file20.write(str(bin(combinations)[2:number_universe+2]).zfill(number_universe))
			file60.write(str(bin(combinations)[2:number_universe+2]).zfill(number_universe))
			file100.write(str(bin(combinations)[2:number_universe+2]).zfill(number_universe))
			spacetext+=1
			
			if spacetext%20 == 0:
			    file20.write('\n')
			if spacetext%40 == 0:
			    file60.write('\n')
			if spacetext%100 == 0:
			    file100.write('\n')
			
		
		combinations = combinations - 1

		if combinations == 0: 
			while auxpot > 0:
				file.write("0")
				auxpot = auxpot - 1
			spacetext+=1
			if spacetext%20 == 0:
			    file20.write('\n')
			if spacetext%40 == 0:
			    file40.write('\n')
			if spacetext%100 == 0:
			    file100.write('\n')
			        

	number_universe = number_universe - 1 

	if (number_universe != 0):
		file.write(",")
		
file.write(",ε}")
file.close()
file20.close()
file60.close()
file100.close()
