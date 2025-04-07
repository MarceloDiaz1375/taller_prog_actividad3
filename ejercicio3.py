from random import randint


def crear_vector(a):
    vector = []
    for i in range(a):
        vector.append(randint(-10, 20))
    return vector

def cantidad_enteros():
    while True:
        #cantidad = 0
        try:
            cantidad = int(input("Ingrese la cantidad de numeros que tendra el vector: "))
        except Exception as e:
            cantidad = 0
        if cantidad > 0:
            break
        elif cantidad == 0:
            print("Ingrese un entero positivo")
        else:
            print("Ingrese un entero positivo")
            
    return cantidad

def sumatoria_vector(vector):
    sumatoria = 0
    for a in vector:
        sumatoria += a
    return sumatoria

def sumar_vectores(vector1, vector2):
    vector_resultante = []
    for i in range(len(vector1)):
        vector_resultante.append(vector1[i] + vector2[i])
    return vector_resultante

if __name__ == "__main__":

    print("Vector A")
    cantidad_n = cantidad_enteros()
    print("Vector B")
    cantidad_m = cantidad_enteros()

    vector_a = crear_vector(cantidad_n)
    vector_b = crear_vector(cantidad_m)

    print("\nVector A")
    print(f"Vector A: {vector_a}")
    sumatoria_a = sumatoria_vector(vector_a)
    print(f"Sumatoria vector A: {sumatoria_a}")
    print("\nVector B")
    print(f"Vector B: {vector_b}")
    sumatoria_b = sumatoria_vector(vector_b)
    print(f"Sumatoria vector B: {sumatoria_b}")

    if cantidad_n == cantidad_m:
        suma_vectores = sumar_vectores(vector_a, vector_b)
        print("\nVector resultante de la suma de los vectores A y B:")
        print(suma_vectores)
