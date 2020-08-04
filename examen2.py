# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:34:07 2020

@author: Barona
"""


n = 151
if (n>99 and n<1000):
    c = n/100
    tmp = n%100
    d = tmp/10
    u = tmp%10
    if(int(u)==int(c)):
        res=str(int(u))+str(int(d))+str(int(c))
        print("El numero ingresado: ", n, "no permite apreciar el cambio ",res)
    else:
        res=str(int(u))+str(int(d))+str(int(c))
        print("num ingresado: ", n,"numero resultado: ", res)
else:
    print("Debe ingresar un numero de tres cifras")