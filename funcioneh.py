contactos=[]

def opcion_1():
    print ("AGREGAR CONTACTO")
    nombre=input("Ingrese Nombre: ")
    telefono=int(input("Ingrese Teléfono: "))
    correo=input("Ingrese correo: ")
    contacto={"nombre":nombre,"telefono":telefono,"correo":correo}
    contactos.append(contacto)

def opcion_2():
    if not contactos:
        print("No existen contactos, registre uno en la opción 1!")
    else:
        print("LISTA CONTACTOS")
        for c in contactos:
            print("NOMBRE:",c["nombre"])
            print("TELÉFONO:",c["telefono"])
            print("CORREO:",c["correo"],"\n")

def opcion_3():
    if not contactos:
        print("No existen contactos, registre uno en la opción 1!")
    else:
        nombre_archivo=input("Ingrese nombre del archivo: ")+".csv"
        import csv
        with open(nombre_archivo,"w",newline="") as archivo:
            escritor=csv.DictWriter(archivo,["nombre","telefono","correo"])
            escritor.writerows(contactos)

def opcion_4():
    print("Movistar le da las gracias")
    exit()