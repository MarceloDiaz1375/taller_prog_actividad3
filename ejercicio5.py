def potencia(x, k):
    return x**k

def cantidad_digitos(a):
    #aux = a
    cont = 0
    if a == 0:
        return 1
    else: 
        while a > 0:
            a = a//10
            cont += 1
        return cont

def cantidad_digitos_cadena(a):
    cadena = str(a)
    if a == 0:
        return 1
    elif a > 0:
        return len(cadena)
    else:
        return len(cadena)-1
        
    
def capicua(a):
    cadena_a = str(a)
    if a < 0:
        cadena_a = cadena_a[1::]
    cadena = ""
    if a == 0:
        return True
    elif a > 0:
        if a < 0:
            a = -a
        while a > 0:
            digito = a%10
            cadena += str(digito)
            #digitos.append(digito)
            a = a//10
    if cadena_a == cadena:
        return True
    else:
        return False
    
def capicua_cadena(a):
    cadena1 = str(a)
    cadena2 = ""
    for i in reversed(cadena1):
        cadena2 += i
    if cadena1 == cadena2:
        return True
    else:
        return False

if __name__ == "__main__":
    
    while True:

        print("\n**** Menu de opciones ****\n")
        print("1 - Calcular la potencia K de un número X")
        print("2 - Obtener la cantidad de dígitos de un número X")
        print("3 - Determinar si un número es capicúa")

        opcion = input("\nIngrese el numero de la opcion: ")

        if opcion == "1":
            while True:
                try:
                    x = float(input("Ingrese el numero X: "))
                    break
                except Exception as e:
                    #print(f"\nOcurrio un error: {e}")
                    print("Solo se aceptan numeros reales")

            while True:
                try:
                    k = int(input("Ingrese la potencia K: "))
                    break
                except Exception as e:
                    #print(f"\nOcurrio un error: {e}")
                    print("Solo se aceptan numeros enteros")
            resultado = potencia(x, k)
            print(f"\nLa potencia {k} de {x} es: {resultado}")

        
        elif opcion == "2":
            while True:
                try:
                    x = int(input("Ingrese el numero X: "))
                    break
                except:
                    print("Solo se aceptan numeros enteros")
            resultado = cantidad_digitos_cadena(x)
            print(f"\nLa cantidad de digitos de {x} es: {resultado}")            
        
        elif opcion == "0":
            break
        else:
            print("Opcion incorrecta")

    print("Programa finalizado")
