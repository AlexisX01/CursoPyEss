# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:44:51 2022

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
    
def dayOfYear(year, month, day):
    
    if month in range(1,13) and (year>0 and year<=2022) and (day > 0 and day <= daysInMonth(year,month)):
        sum_mes=0
        for mes in range(1,month):
            sum_mes=sum_mes+ daysInMonth(year,mes)
        return sum_mes+day
    else: 
        return None
    
print(dayOfYear(2000, 12, 31))
print(dayOfYear(2000, 12, 27))
            
                
            