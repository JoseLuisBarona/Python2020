# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:44:26 2020

@author: Barona
"""


def mensaje(edad):
    mensaje =""
    if edad >= 18 and edad <=20:
        mensaje = "De 18 a 20 años"
    elif edad >= 16 and edad <= 17:
        mensaje = "De 16 a 17 años"
    elif edad <= 10 and edad <= 15:
        mensaje = "De 10 a 18 años"
    elif edad < 9 or edad > 20:
        mensaje = "Edad fuera de rango"
    return mensaje
edad = 2
print("Mensaje de salida", mensaje(edad))