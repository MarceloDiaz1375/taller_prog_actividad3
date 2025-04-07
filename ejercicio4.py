def lista_palabras(texto):
    lista_palabras = texto.split(" ")
    return lista_palabras


def contar_vocales(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    cantidad_vocales = 0
    for letra in texto:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

def contar_consonantes(texto):
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    cantidad_consonantes = 0
    for letra in texto:
        if letra in consonantes:
            cantidad_consonantes += 1
    return cantidad_consonantes

if __name__ == "__main__":

    texto = input("Ingrese una oracion: ")
    texto = texto.lower()

    cantidad_vocales = contar_vocales(texto)
    cantidad_consonantes = contar_consonantes(texto)

    print(f"\nCantidad de vocales en el texto: {cantidad_vocales}")
    print(f"\nCantidad de consonantes en el texto: {cantidad_consonantes}")

    print(lista_palabras(texto))

