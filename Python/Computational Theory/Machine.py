#Author Montes Martínes Jesús Iori
import random
import time
from datetime import datetime

def verifydata():
    file = open('Stades.txt','w')
    filetwo = open('strings.txt','r')
    fileaccepted = open('accepted.txt','w')
    filewrong = open('wrong.txt','w')
    
    for c in filetwo:
        i=0
        stade=0
        file.write(c)
        while c[i] != '\n':
            if (stade == 0 and c[i] == "0"):
                stade = 1
                file.write("|q0|--->|q1| \n")
                i+=1
                continue
            if (stade == 0 and c[i] == "1"):
                stade = 3
                file.write("|q0|--->|q1| \n")
                i+=1
                continue
            if (stade == 1 and c[i] == "0"):
                stade = 0
                file.write("|q1|--->|q0| \n")
                i+=1
                continue
            if (stade == 1 and c[i] == "1"): 
                stade = 2
                file.write("|q1|--->|q2| \n")
                i+=1
                continue
            if (stade == 2 and c[i] == "1"):
                stade = 1
                file.write("|q2|--->|q1| \n")
                i+=1
                continue
            if (stade == 2 and c[i] == "0"): 
                stade = 3
                file.write("|q2|--->|q3| \n")
                i+=1
                continue
            if (stade == 3 and c[i] == "0"):
                stade = 2
                file.write("|q3|--->|q2| \n")
                i+=1
                continue
            if (stade == 3 and c[i] == "1"):
                stade = 0
                file.write("|q3|--->|q0| \n")
                i+=1
                continue
        if (stade == 0):
            fileaccepted.write(c)
        else:
            filewrong.write(c)
    file.close()
    filetwo.close()
    fileaccepted.close()
    filewrong.close()
    

def create_strings():
    file = open('record.txt','a')
    filetwo = open('strings.txt','w')
    start=0
    while start<10:
        string_binary=''
        i=0
        while i<32:
            rand = random.randrange(2)
            string_binary_aux=str(bin(rand)[2:])
            string_binary=string_binary+string_binary_aux
            i+=1
        file.write(string_binary+'\n')
        filetwo.write(string_binary+'\n')
        start+=1
    file.close()
    filetwo.close()
    print('The strings are completed')
    print('you wait one second please')
    time.sleep(1)

repeat=True
while repeat == True:
    state_machine = random.randrange(2)
    binary = str(bin(state_machine)[2:])
    now = str(datetime.now())
    
    if( binary == '1'):
        file = open('record.txt','a')
        print('The machine is on')
        file.write('The machine is on '+now+'\n')
        file.close()
        create_strings()
        verifydata()
        
    else:
        file = open('record.txt','a')
        print('The machine is off')
        file.write('The machine is off '+now+'\n')
        file.close()
        repeat=False
