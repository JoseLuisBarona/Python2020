# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:29:04 2020

@author: Barona
"""
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, )

for x in dct.keys():
    print(dct[x][1], end="")
