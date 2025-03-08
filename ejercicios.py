# Lista de letras del alfabeto en mayúsculas
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Función que imprime el número y las letras en posiciones múltiplos de num
def ejerciciouno():
    print("             ")
    num = int(input("Ingrese un número: "))  # Recibe un número desde la consola
    print("Primer ejercicio")
    print("Numero:", num)
    # ALPHABET[i] recorre cada uno de los elementos de la lista ALPHABET
    # range(num - 1, len(ALPHABET), num) recorre desde el inicio con num-1 hasta el final de la lista ALPHABET con saltos segun num
    print("Letras en posiciones múltiplos de", num, ":", [ALPHABET[i] for i in range(num - 1, len(ALPHABET), num)])
    print("             ")

# Dada una frase averiguar cuantas vocales tiene y mostrarlas
def ejerciciodos():
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    frase = input("Ingrese una frase: ")  # Recibe una frase desde la consola
    print("Frase:", frase)
    # range(len(frase)) genera una secuencia de índices que van desde 0 hasta la longitud de la frase
    # frase[i] recorre cada uno de los elementos de la frase
    # vowels.count(frase[i]) cuenta cuantas veces aparece la letra en la lista
    print("Número de vocales:", sum([vowels.count(frase[i]) for i in range(len(frase))]))
    print("             ")

# Ejecutar la función
ejerciciouno()
ejerciciodos()

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
