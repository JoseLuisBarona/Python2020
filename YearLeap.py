# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:50:33 2020

@author: Barona
"""
##Jose Luis Barona #Grupo 2 
def isYearLeap(year):
    if year % 4 != 0:
        return False 
        #print("NO es LeapYear")
    elif year % 100 != 0:
        return True
        #print("SI es LeapYear")
    elif year % 400 != 0:
        return False 
        #print ("No es LeapYear")
    else:
        return True
        #print ("SI es LeapYear")
y = isYearLeap(1987)
print(y)

testdata = [2019, 2020, 2016, 1987]
testresults = [False, True, True, False]
#print (isYearLeap(2020))
for i in range(len(testdata)):
    yr = testdata[i]
    print (yr, "-> ",end=" ")
    result = isYearLeap(yr)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")