# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:09:05 2020

@author: Barona
"""


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
localizaciòn=input("Ingrese su ubicaciòn donde reside: ")
edad=input("Ingrese su edad: ")
print("Hola mucho gusto, mi nombre es "+nombre + apellido+" yo tengo "+edad+ " años" 
      " actualmente resido en "+localizaciòn+ " es un lugar muy hermoso, me encanta allí." )
edad= int(edad)
if edad >=10 and edad <=17:
    print("Usted es menor de edad")
elif edad>=18 and edad <=30:
    print("Usted es mayor de edad")
elif edad >=31 and edad <=50:
    print ("Es usted adulto")
elif edad >=51 and edad <=120:
    print ("Es usted un adulto mayor")
else:
    print("Es usted un niño")
    

