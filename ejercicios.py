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

