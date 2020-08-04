# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:54:41 2020

@author: Barona
"""


x = 5
#print(("El valor  de x es: ",x)
print ("El valor de x es: " + str(x))
x=str(x)
print("\n" *2)
print(type(x))
x=str(x)
print(type(x))
x=int(x)
print(type(x))
x=float(x)
print(type(x))
x=bool(x)
print(type(x))
x=int(x)
print(type(x))
#print("El valor de x es: )

print (type(558.33))
print("\n"*1)
pi= 22/7
print(pi)
3.142857142857143

print("{: .4f}".format(pi))
3.14
print("\n"*1)
hostnames=["R1","R2","R3","S1","S2"]
print(type(hostnames))
print("\n"*1)
print(len(hostnames))
print(hostnames)
print(hostnames[0])
print(hostnames[1])
print(hostnames[2])
print(hostnames[3])
print(hostnames[4])
print("\n")
print(hostnames[-1])
print(hostnames[-2])
print("\n")
#print(hostnames[5]) #error
#print(hostnames[-6]) #error
hostnames[1]="RTR1"
del hostnames[4]