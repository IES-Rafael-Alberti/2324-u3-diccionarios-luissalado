'''

Escribir un programa que pregunte una fecha en 
formato dd/mm/aaaa y muestre por pantalla la misma 
fecha en formato dd de <mes> de aaaa donde <mes> 
es el nombre del mes.


'''


def obtener_nombre_mes(numero_mes):
    meses = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
        7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }

    return meses.get(numero_mes)

def fecha_input():
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")

    try:

        dia, mes, anio = map(int, fecha.split('/'))

        nombre_mes = obtener_nombre_mes(mes)

        if nombre_mes:

            nueva_fecha = f"{dia} de {nombre_mes} de {anio}"
            print(f"{nueva_fecha}")
        else:
            print("Mes no válido")
    except ValueError:
        print("Formato de fecha incorrecto")

if __name__ == "__main__":
    fecha_input()