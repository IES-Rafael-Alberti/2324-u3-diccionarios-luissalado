'''
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
una divisa y muestre su símbolo o un mensaje de aviso si la 
divisa no está en el diccionario.

'''

def divisa(pedir):
    d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    if pedir in d:
        return d[pedir]
    else:
        raise ValueError
    
if __name__ == "__main__":
    
    
    try:
        pedir = input("Dime una divisa: ")
        print(divisa(pedir))
        
    except:
        print('ERROR')
    
    
    