from random import randint

matriz = [
    ["X", "O", "7", "X", "O", "7", "X", "O", "7"],
    ["O", "7", "X", "O", "7", "X", "O", "7", "X"],
    ["7", "X", "O", "7", "X", "O", "7", "X", "O"]
]

fichas = 0

def rotar(matriz, rotaciones):
    matriz2 = []
    cont = 0
    for vector in matriz:
        vector2 = vector[-rotaciones[cont]:] + vector[:-rotaciones[cont]]
        matriz2.append(vector2)
        cont += 1
    return matriz2

while True:
    print("\n***** Máquina tragamonedas *****")
    print("1 - Tirar de la palanca")
    print("0 - Salir")

    opcion = input("\nIngrese el numero de la opcion elegida: ")

    if opcion == "1":
        rotaciones = [randint(0, 9), randint(0, 9), randint(0, 9)]
        #rotaciones = [5, 3, 1]
        resultado = rotar(matriz, rotaciones)
        print("\nResultado: ")
        for lista in resultado:
            print(lista)
        if resultado[0][0] == resultado[1][0] and resultado[2][0] == resultado[1][0]:
            if resultado[0][0] == "O":
                print("\nGano 100 fichas")
                fichas += 100
            elif resultado[0][0] == "7":
                print("\nGano 1000 fichas")
                fichas += 1000
            elif resultado[0][0] == "X":
                print("\nGano 10 fichas")
                fichas += 10
        
    elif opcion == "0":
        break

    else:
        print("\nOpcion incorrecta, ingrese el numero nuevamente.")
    
print("\nJuego finalizado")
print(f"\nFichas ganadas: {fichas}")