# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:32:40 2022

@author: Usuario
"""

def isYearLeap(year):
    if year%4 == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    num_dias=[31,28,31,30,31,30,31,31,30,31,30,31] #Numero de días año normal
    
    if month in range(1,13) and (year>0 and year<=2022): #Validar mes y año
        if month == 2:  #Si es Febrero
            if isYearLeap(year): #Si es año bisciesto 29 días
                return 29
            else:
                return 28
        else:       #Asigno valor de mesez
                return num_dias[month-1]
        return None 
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

        
        