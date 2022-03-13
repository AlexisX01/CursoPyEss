# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:37:09 2022

@author: Alexis Criollo
"""

print("Ingrese sus datos para la entrega del producto ") 
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
ubic=input("Ingrese su ubicación: ")

edad=int(input("Ingrese su edad: "))
espacio=" "

print("\n")
print("La entrega se realizará a nombre de "+nombre+espacio+apellido+espacio+
      "de"+ espacio+ str(edad) +espacio+ "años de edad"+ espacio+
      "a la dirección de "+ubic)

# 6 niño adolescente adulto adulto mayor
if edad>=5 and edad<=6:
    print("Usted es un niño.")
elif edad>6 and edad<=17:
    print("Usted es un adolescente.")
elif edad>17 and edad<=64:
    print("Usted es un adulto.")
elif edad>64 and edad<100:
    print ("Usted es un adulto mayor.")
else:
    print("Edad ingresada no valida.")
