import os, time
from funcioneh import *
while True:
    os.system("cls")
    print ("MENÚ CONTACTOS")
    print ("1.Agregar contacto\n2.Ver contactos\n3.Exportar archivo\n4.Salir")
    opc=int(input("Ingrece opcion: "))
    os.system("cls")
    if opc ==1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(3)