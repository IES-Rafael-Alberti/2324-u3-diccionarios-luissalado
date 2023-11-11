'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.



'''

def menu():
    print("\n--- Menú ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

def anadir_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la direccion del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    preferente = input("¿Es un cliente preferente? (True/False): ").lower() == 'true'

    cliente = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

    base_datos[nif] = cliente
    print("Cliente añadido correctamente.")

def eliminar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente a eliminar: ")
    if nif in base_datos:
        del base_datos[nif]
        print("Cliente eliminado correctamente.")
    else:
        print("El cliente no existe en la base de datos.")

def mostrar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente a mostrar: ")
    if nif in base_datos:
        cliente = base_datos[nif]
        print("\nDatos del cliente:")
        print(f"NIF: {nif}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Direccion: {cliente['direccion']}")
        print(f"Telefono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Preferente: {cliente['preferente']}")
    else:
        print("El cliente no existe en la base de datos.")

def listar_todos_clientes(base_datos):
    print("\nLista de todos los clientes:")
    for nif, cliente in base_datos.items():
        print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

def listar_clientes_preferentes(base_datos):
    print("\nLista de clientes preferentes:")
    for nif, cliente in base_datos.items():
        if cliente['preferente']:
            print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

def muestra():
    base_datos_clientes = {}

    while True:
        menu()
        opcion = input("Seleccione una opcion (1-6): ")

        if opcion == '1':
            anadir_cliente(base_datos_clientes)
        elif opcion == '2':
            eliminar_cliente(base_datos_clientes)
        elif opcion == '3':
            mostrar_cliente(base_datos_clientes)
        elif opcion == '4':
            listar_todos_clientes(base_datos_clientes)
        elif opcion == '5':
            listar_clientes_preferentes(base_datos_clientes)
        elif opcion == '6':
            print("Programa terminado.")
            break
        else:
            print("Opción no valida")

if __name__ == "__main__":
    
    muestra()
