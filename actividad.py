# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:41:19 2020

@author: Barona
"""


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
localizaciòn=input("Ingrese su ubicaciòn donde reside: ")
edad=input("Ingrese su edad: ")
edad= int(edad)
if edad >=1 and edad <=17:
    print("Usted es menor de edad")
if edad>=18 and edad <=30:
    print("Usted es mayor de edad")
if edad >=31 and edad <=50:
    print ("Es usted adulto")
if edad >=51 and edad <=100:
    print ("Es usted un adulto mayor")
    
    

