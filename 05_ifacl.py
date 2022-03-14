
acl=int(input("Ingrese el # del ACL: "))
if acl>1 and acl<=99:
    print("La ACL es Standar")
elif acl >=100 and acl<=199:
    print("La ACL es Extendida")
else:
    print("El # ingresado no es un ACL válido")
