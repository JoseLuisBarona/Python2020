# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:21:53 2020

@author: Barona
"""


a = 4
b = 3 
c = 6
if (c> b+b):
    print("No se trata de un triangulo")
elif (c**2 == a**2 + b**2):
    print("Es un triangulo rectangulo")
elif(c**2 > a**2 + b**2):
    print("se forma un triangulo obtusangulo")
elif (c**2 < a**2 + b**2):
    print("se forma un triangulo acutangulo")