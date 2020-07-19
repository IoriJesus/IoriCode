import sys
import random
import os.path as path
from os import remove
from matplotlib import pyplot as plt

def datas_of_file():
    f = open("binary primes.txt", "r")
    for linea in f:
        print(linea)
    f.close()
def Makegrafic():
    cor= open("binary primes.txt","r")
    y=[]
    x=[]
    z=0
    c= cor.readlines()

    for c in c:
        i=0
        j=0
        while c[i]!='\n':
            if c[i]=='1':
                j+=1
            i +=1
        y.append(j)
        x.append(z)
        z+=1

    plt.plot(x, y, color='red', linewidth=3)
    plt.scatter(x, y, color='darkblue', marker='^')
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

def grafic(x,y):
    f = open("dataGrafic.txt", "a")
    f.write(str(x)+' '+str(y)+'\n')
    f.close()

def add_file(prime_binary):
    f=open('binary primes.txt','a')
    f.write(prime_binary +'\n')
    f.close()

def number_to_binary(number,x):
    binary=''
    y=0
    
    while number > 0:
        
        if number%2 == 0:
            binary ='0'+ binary
        else:
            binary ='1' + binary
            y+=1
            
        number=number//2
        
    add_file(binary)
    grafic(x,y)

def number_prime(number):
    x=0
    for i in range(number):
        i=i+1
        prime=True
        
        if i%2 == 0 and i !=2:
            prime=False
        if i%3 == 0 and i!=3:
            prime=False
        if i%5 == 0 and i!=5:
            prime=False
        if i%7 == 0 and i!=7:
            prime=False
            
        if prime == True and i != 1:
            x+=1
            number_to_binary(i,x)
            
        if(i == number):
            datas_of_file()
            Makegrafic()

def removefiles():
    if path.exists('binary primes.txt'):
        remove('binary primes.txt')
    if path.exists('dataGrafic.txt'):
        remove('dataGrafic.txt')
        
def verify_date():
    number = input('write one number:')
    
    if number == '':
            number=random.randrange(1000000)
            print(number)
        
    try:
    	number = int(number)
    	if number > 1:
    	    return number
    	else:
    	    if number == 1:
    	        print('zero and one don´t are numbers primes')
    	        sys.exit(0)
    	        
    	    if number == 0:
    	        print('zero don´t is a number prime')
    	        sys.exit(0)
    	        
    	    if number < 0:
    	        print('This program don´t accepted numbers smaller than 0')
    	        sys.exit(1)
    except ValueError:
        print("datas don´t valid")
        sys.exit(1)

number=verify_date()
removefiles()
number_prime(number)
