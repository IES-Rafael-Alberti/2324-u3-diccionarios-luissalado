import re

'''

Escribir un programa que pregunte al usuario su nombre, edad, 
dirección y teléfono y lo guarde en un diccionario. Después
debe mostrar por pantalla el mensaje <nombre> tiene <edad> 
años, vive en <dirección> y su número de teléfono es <teléfono>.

'''

d ={}

def nombre_input(nombre):
    d['nombre'] = nombre

def edad_input(edad):
    if str.isnumeric(edad):
        d['edad'] = edad
    else:
        return ValueError
    
def direccion_input(direccion):
    d['direccion'] = direccion
    
def telefono_input(telefono):
        d['telefono'] = telefono
        
def genera_mensaje(nombre,edad,telefono,direccion):
    nombre_input(nombre)
    edad_input(edad)
    direccion_input(direccion)
    telefono_input(telefono)
    
    return f" {d['nombre'] } tiene {d['edad']} años, vive en {d['direccion']} y su numero de telefono es {d['telefono']} "

    


if __name__ == "__main__":
    
    
    try:
        nombre = input("Como te llamas: ")
        edad = input("Dime tu edad: ")
        direccion = input("Dame tu direccion: ")
        telefono = input("Dame tu telefono: ")
        
        print(genera_mensaje(nombre,edad,telefono,direccion))
    except:
        print("ERROR")