# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:41:53 2020

@author: Barona
"""


def sumaMatriz(A,B):
   
    numFilasA = len(A)
    numFilasB = len(B)
    numColumnasA = len(A[0])
    numColumnasB = len(B[0])
    
    if numFilasA == numFilasB and numColumnasA == numColumnasB:
        C = newMatrix(numFilasA, numColumnasA, 0) 
        for i in range(numFilasA): 
            for j in range(numColumnasA):
                
                C[i][j] = A[i][j] + B[i][j]
                
    return C

def show_matrix(M):
        """ Imprime los valores almacenados en la matriz """
        filas = len(M)
        columnas = len(M[0])
        for i in range(filas):
            for j in range(columnas):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(M[i][j]), sep=',', end='')
            print('|\n')