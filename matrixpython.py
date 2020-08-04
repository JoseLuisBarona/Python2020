# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:44:11 2020

@author: Barona
"""


matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0]]
for i in range (0,5):
    for j in range(0,6):
        print("Ingrese el valor de la posición: ",i,j)
        matrix[i][j]=int(input())
print(matrix)