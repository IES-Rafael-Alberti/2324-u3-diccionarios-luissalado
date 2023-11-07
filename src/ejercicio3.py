'''

Escribir un programa que guarde en un diccionario los precios 
de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese 
número de kilos de fruta. Si la fruta no está en el diccionario 
debe mostrar un mensaje informando de ello.

'''


d = {'platano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}


def pedido_input():
    pedir = input("Dime una fruta: ")
    if pedir in d:
        return d[pedir]
    else:
        return KeyError

def kilos():
    kilos = input("Dime los kilos que quieras: ")
    fruta = pedido_input()
    
    total = kilos * fruta
    return total

def genera_mensaje():
    pedido_input()
    kilos()
    
    return f""
    
