# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:39:47 2020

@author: Barona
"""


while True:
    print("1. Convertir F a C")
    print("2. Convertir C a F")
    print("3. Salir")
    x= input("Escoja una opcion ")
    if x=="1":
        f=int(input("Digite grados F "))
        c=5/9*(f-32)
        print("La temperatura promedio en F es: ", c)
    elif x=="2":
        c=int(input("Digite grados C "))
        f= 9/5*c+32;
        print(f)
    elif x=="3":
        
        break