import json
from datetime import date

listaCompras=[]
with open("./Compras.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaCompras=json.load(files)

listaEmpleados=[]
with open("./Empleados.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaEmpleados=json.load(files)

listaMedicamentos=[]
with open("./Medicamentos.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaMedicamentos=json.load(files)

listaPacientes=[]
with open("./Pacientes.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaPacientes=json.load(files)

listaProveedores=[]
with open("./Proveedores.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaProveedores=json.load(files)

listaVentas=[]
with open("./Ventas.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaVentas=json.load(files)



def guardarCompras(miDato):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("compras.json","w") as outfile:
        json.dump(miDato,outfile)

def guardarVentas(miDato):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Ventas.json","w") as outfile:
        json.dump(miDato,outfile)

def guardarEmpleados(miDato):# se crea una funcion para guardar los cambios que le realizemos al Json
    with open("Empleados.json","w") as outfile:
        json.dump(miDato,outfile)

def Guardarventa(fecha,nombre,direccion,nombreEmpleado,cargoEmpleado,medicamentosVendidos):# se crea una función para guardar las ventas realizadas en el json
    venta={
        "fechaVenta": fecha,
        "paciente": {
            "nombre": nombre,
            "direccion": direccion
        },
        "empleado": {
            "nombre": nombreEmpleado,
            "cargo": cargoEmpleado
        },
        "medicamentosVendidos": []
    }
    for medicamento,cantidad,precio in medicamentosVendidos:
        venta["medicamentosVendidos"].append({
            "nombre": medicamento,
            "cantidad":cantidad,
            "preciodeventa": precio
        })
    listaVentas.append(venta)
    guardarArchivo("Ventas.json",listaVentas)

def guardarArchivo(archivo,datos):# Se crea una función que permite guardar todos los cambios en los json 
    with open(archivo,"w", encoding="utf-8") as outfile:
        json.dump(datos,outfile, indent=4)
def GuardarCompraa(fecha,nombre,contactoProveedor,medicamentosComprados):# se crea una función para guardar las ventas realizadas en el json
    venta={
        "fechaVenta": fecha,
        "proveedor": {
            "nombre": nombre,
            "contacto":contactoProveedor
        },
        "medicamentosComprados": []
    }
    for medicamento,cantidad,precio in medicamentosComprados:
        venta["medicamentosComprados"].append({
            "nombre": medicamento,
            "cantidad":cantidad,
            "preciodeventa": precio
        })
    listaCompras.append(venta)
    guardarArchivo("Compras.json",listaCompras)
def Guaedarrcompra(fecha,nombre,contactoProveedor,medicamentosComprados):# Se crea una función para guardar las compras en el json 
    compra={
        "fechaCompra": fecha,
        "proveedor": {
            "nombre": nombre,
            "contacto": contactoProveedor
        },
        "medicamentosComprados": []
    },
    for producto,cantidad,precio in medicamentosComprados:
        compra["medicamentosComprados"].append({
            "nombreMedicamento": producto,
            "cantidadComprada":cantidad,
            "precioCompra": precio
        })
    listaCompras.append(compra)
    guardarArchivo("compras.json",listaCompras)


menuu=True
while menuu==True:
    print("########################################################")
    print("------------- Gestión de Ventas y Compras -------------")# Se crea el menu principal el cual cuenta con 4 opciones 
    print("########################################################")
    print("(1) Ventas")
    print("(2) Compras")
    print("(3) Finalizar programa")
    opcion=int(input("Ingresa la opción deseada: "))
    if opcion==1:
        print("#########################################")
        print("---------------- Ventas ----------------")
        print("#########################################")
        fecha=str(date.today())
        nombre=input("nombre del cliente: ")
        direccion=input("Direccion del cliente: ")
        nombreEmpleado=input("Nombre del empleado: ")
        cargoEmpleado=input("Cargo del empleado: ")
        medicamentosVendidos=[]
        buliano=True
        while buliano==True:# se utiliza un bucle while para crear los productos que el usuario requiera y asi añadirlos al json
            medicamento=input("escribe el nombre del producto: ")
            cantidad=int(input("cantidad: "))
            for i in listaMedicamentos:# se crea una función para extraer el precio del producto  anteriormente escrito por el usuario
                if medicamento== i["nombre"]:
                    precio=i["precio"]
            medicamentosVendidos.append((medicamento, cantidad, precio))
            seguir=int(input("si deseas agregar otro producto escribe (si=1) o si deseas finalizar escribe (no=2)"))
            if seguir==1:
                buliano=True
            elif seguir==2:
                buliano=False
        Guardarventa(fecha, nombre, direccion, nombreEmpleado, cargoEmpleado,medicamentosVendidos)



    elif opcion==2:# Se realiza la opción 2 del menu principal
        print("#######################################")
        print("---------------- Compras ----------------")
        print("#######################################")

        fecha=str(date.today())
        nombre=input("nombre del proveedor: ")
        contactoProveedor=input("Escribe el contacto del proveedor: ")
        medicamentosComprados=[]
        buliano=True

        while buliano==True: # se utiliza un bucle while para crear los productos que el usuario requiera y asi añadirlos al json
            medicamento=input("escribe el nombre del producto: ")
            cantidad=int(input("cantidad: "))
            precio= float(input("precio de compra: "))
            medicamentosComprados.append((medicamento,cantidad,precio))
            seguir=int(input("si deseas agregar otro producto escribe (si=1) o si deseas finalizar escribe (no=2)"))
            if seguir==2:
                break
        GuardarCompraa(fecha, nombre, contactoProveedor,medicamentosComprados)


    else:
        menuu=False

# Programa desarrollado por Camilo Machuca Vega
