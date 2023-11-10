'''

Escribir un programa que gestione las facturas 
pendientes de cobro de una empresa. Las facturas se 
almacenarán en un diccionario donde la clave de cada 
factura será el número de factura y el valor el coste 
de la factura. El programa debe preguntar al usuario 
si quiere añadir una nueva factura, pagar una existente
o terminar. Si desea añadir una nueva factura se 
preguntará por el número de factura y su coste y se 
añadirá al diccionario. Si se desea pagar una factura
se preguntará por el número de factura y se eliminará 
del diccionario. Después de cada operación el programa 
debe mostrar por pantalla la cantidad cobrada hasta el 
momento y la cantidad pendiente de cobro.

'''


def gestionar_facturas():
    facturas = {}
    cobrado = 0

    while True:
        print("\n--- Menú ---")
        print("1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Terminar")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            numero_factura = input("Ingrese el número de factura: ")
            costo_factura = float(input("Ingrese el coste de la factura: "))

            facturas[numero_factura] = costo_factura
            cobrado += costo_factura

        elif opcion == '2':
            numero_factura = input("Ingrese el número de factura a pagar: ")

            if numero_factura in facturas:
                costo_factura = facturas.pop(numero_factura)
                cobrado += costo_factura
                print(f"Factura {numero_factura} pagada.")
            else:
                print("La factura no existe.")

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Intente de nuevo.")


        print(f"\nCantidad cobrada hasta el momento: {cobrado}")
        print(f"Cantidad pendiente de cobro: {sum(facturas.values())}")

if __name__ == "__main__":
    gestionar_facturas()