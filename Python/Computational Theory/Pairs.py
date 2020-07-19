#Author Montes Martínez Jesús Iori
import sys
import random

file = open('Stades.txt','w')

def verify_date():
    string_binary = input('write one string:')
    
    if string_binary == '':
        rand = random.randrange(10000000000)
        string_binary = str(bin(rand)[2:])
        print(string_binary)
        return string_binary
            
            
    for i in string_binary:
        if (i == '0' or i =='1'):
            if(i == string_binary):
                print('your string is valid')
                
        else:
            print('your string is invalid for:',i)
            sys.exit(1)
            
    return string_binary

string_binary=verify_date()
stade=0 
file.write("|statex|--reed data->|statey| \n")

for i in string_binary:

	if (stade == 0 and i == "0"): 
		stade = 1
		file.write("|q0|--->|q1| \n")
		continue
	if (stade == 0 and i == "1"):
		stade = 3
		file.write("|q0|--->|q1| \n")
		continue

	if (stade == 1 and i == "0"):
		stade = 0
		file.write("|q1|--->|q0| \n")
		continue
	if (stade == 1 and i == "1"): 
		stade = 2
		file.write("|q1|--->|q2| \n")
		continue

	if (stade == 2 and i == "1"):
		stade = 1
		file.write("|q2|--->|q1| \n")
		continue
	if (stade == 2 and i == "0"): 
		stade = 3
		file.write("|q2|--->|q3| \n")
		continue

	if (stade == 3 and i == "0"):
		stade = 2
		file.write("|q3|--->|q2| \n")
		continue
	if (stade == 3 and i == "1"): 
		stade = 0
		file.write("|q3|--->|q0| \n")
		continue
file.close()

if (stade == 0):
	print('the string',string_binary,'is pair')
else:
	print('the string',string_binary,'don´t is pair')
