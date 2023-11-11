'''

Escribir un programa que cree un 
diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español 
e inglés separadas por dos puntos, y cada par 
<palabra>:<traducción> separados por comas. 
programa debe crear un diccionario con las
palabras y sus traducciones. Después pedirá una 
frase en español y utilizará el diccionario para 
traducirla palabra a palabra. Si una palabra no está 
en el diccionario debe dejarla sin traducir.


'''

def crear_diccionario():
    entrada_usuario = input("Introduce las palabras en español e ingles separadas por dos puntos, y cada par separado por comas: ")
    pares = entrada_usuario.split(',')
    
    diccionario = {}
    for par in pares:
        palabra, traduccion = par.split(':')
        diccionario[palabra.strip()] = traduccion.strip()

    return diccionario

def traducir_frase(frase, diccionario):
    palabras = frase.split()
    traduccion = [diccionario.get(palabra, palabra) for palabra in palabras]
    return ' '.join(traduccion)

def frase():
    diccionario = crear_diccionario()
    print("\nDiccionario creado:")
    print(diccionario)

    frase_espanol = input("\nIntroduce una frase en español: ")
    frase_traducida = traducir_frase(frase_espanol, diccionario)

    print("\nFrase traducida:")
    print(frase_traducida)

if __name__ == "__main__":
    
    frase()

