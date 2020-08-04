# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:40:37 2020

@author: Barona
"""


fecha= int(input("Ingrese año para determinar si es bisiesto o no: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print("Verdadero",fecha)
else:
    print("Falso",fecha)
