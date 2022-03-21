# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:55:25 2022

@author: Usuario
"""

file=open("devices.txt",mode="a")

while True:
    newItem=input("Ingrese un equipo a añadir: ")
    if newItem.lower() == "exit":
        print("All done!")
        file.close()
        break
    file.write(newItem + "\n")


file=open("devices.txt")
for item in file:
    print(item)
file.close()





