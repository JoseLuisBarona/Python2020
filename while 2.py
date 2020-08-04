# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:49:21 2020

@author: Barona
"""


dato=int(input("Ingrese el numero de veces que contare: "))
contador=1
acumulador=0 
while contador <=dato:
    print(contador, end=" ")
    acumulador+=contador
    contador+=1
print("\n"*2)
print("la suma de los numeros es: ",acumulador)