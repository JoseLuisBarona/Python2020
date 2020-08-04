# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:22:36 2020

@author: Barona
"""


acl = input("Ingrese el numero de ACL: ")
acl= int (acl)
print("\n"*2)
if acl >= 1 and acl <= 99:
    print ("Este ACL es STANDARD")
elif acl >=100 and acl <= 199:
    print("Este ACL es EXTENDIDA")
else:
    print("Esto no es ACL")
