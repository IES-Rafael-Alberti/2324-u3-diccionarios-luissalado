'''

Escribir un programa que guarde en un diccionario los precios 
de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese 
número de kilos de fruta. Si la fruta no está en el diccionario 
debe mostrar un mensaje informando de ello.

'''



d = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}


def pedido_input():
    pedir = input("Dime una fruta: ")
    if pedir in d:
        return pedir  
    else:
        return None  


def kilos(fruta):
    kilos = float(input("Dime los kilos que quieras: ")) 
    if fruta in d:
        precio_por_kilo = d[fruta]
        total = kilos * precio_por_kilo
        return total
    else:
        return None  


def genera_mensaje():
    fruta = pedido_input()

    if fruta is not None:
        total = kilos(fruta)
        if total is not None:
            print(f"El total es: {total}")
        else:
            print("La fruta no esta")
    else:
        print("La fruta no esta")


if __name__ == "__main__":
    genera_mensaje()



