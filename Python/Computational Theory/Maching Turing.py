import sys
import time
import random
from random import randint
from datetime import datetime


state = 0
position_headband = 0
space_in_headband = True
time = str(datetime.now())
file = open('MachingTuringData.txt','a')

headband = input('Ingrese la cadena a evaluar o de click  en Intro para generar una cadena automatica: ')
file.write('Test at '+time+'\n')

if headband  == '':
    rand = random.randrange(10000)
    headband = str(bin(rand)[2:])

headband = headband + ' '

while(space_in_headband):
    
    search_one = True
    return_to_zero = True
    
    if(headband[position_headband]  == '1' and state == 0):
        file.write('State: '+str(state)+'\n')
        file.write('Esta cadena no existe en el lenguaje'+'\n')
        break
    
    if(headband[position_headband] == '0'):
        file.write('State: '+str(state)+'\n')
        headband = headband.replace(headband[position_headband],'X',1)
        file.write('q'+str(state)+' = X'+'\n')
        file.write(headband+'\n')
        print(headband)
        
        while(search_one):
            
            if(headband[position_headband] == '1'):
                headband = headband.replace(headband[position_headband],'Y',1)
                file.write('q'+str(state)+' = Y'+'\n')
                file.write(headband+'\n')
                print(headband)
                search_one = False
            else:
                position_headband+=1
                
                if(headband[position_headband] == ' '):
                    file.write('Esta cadena no existe en el lenguaje'+'\n')
                    break
                    
        while(return_to_zero):
            
            if(headband[position_headband] == 'X'):
                position_headband+=1
                return_to_zero = False
            else:
                position_headband-=1
                
    if(headband[position_headband] == 'Y'):
        
        while(search_one):
            
            if(headband[position_headband] == '1'):
                file.write('Esta cadena no existe en el lenguaje'+'\n')
                search_one = False
                space_in_headband = False
            else:
                position_headband+=1
                
                if(headband[position_headband] == ' '):
                    file.write('Esta cadena pertenece al lenguaje'+'\n')
                    search_one = False
                    space_in_headband = False
        
    state+=1

file.close()        
print(headband)



