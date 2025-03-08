def ejerciciotres():
    cadena = 'El mejor regalo? El perdon'
    #quitar los signos de puntuacion
    import string
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    #divide el texto en palabras
    lista = cadena.split()
    print(lista)
    #quitar las palabras
    cadena_nueva = lista
    print(cadena_nueva)
    cadena_nueva.pop(2)
    print(cadena_nueva)
    cadena_nueva.pop(2)
    print(cadena_nueva)
    # convertir lista en textro
    nueva_palabra = ' '.join(cadena_nueva)
    print("la palabra nueva es: ")
    print(nueva_palabra)  # "El mejor perdon"
        


def ejerciciocuatro():
    # crea valores aleatrios
    numeros = list(range(1, 11))
    # Elevar cada valor al cuadrado
    cuadrado = [numero ** 2 for numero in numeros]
    print("el cuadrado de los valores de la lista es: ")
    print(cuadrado) 
    print("el cubo de los valores de la lista es: ")
    cubo = [numero ** 3 for numero in numeros]
    print(cubo)


ejerciciotres()
ejerciciocuatro()
