     
def es_mayor(num, num2):
    if num > num2:
        return True
    else:
        return False
    
def ingresar_numero():
    try:
        num = float(input("Ingrese un numero: "))
        return num
    except:
        print('Solo ingrese numeros')
        return None
    
def mayor_de_tres(num, num2, num3):

    if es_mayor(num, num2) and es_mayor(num, num3):
        return num
    elif es_mayor(num2, num) and es_mayor(num2, num3):
        return num2
    elif es_mayor(num3, num) and es_mayor(num3, num2):
        return num3
    else:
        print('Los 3 numeros son iguales')
        return num


if __name__ == '__main__':
    numero = ingresar_numero()
    numero2 = ingresar_numero()
    numero3 = ingresar_numero()
    print(mayor_de_tres(numero, numero2, numero3))
    suma = None+5
    print(suma)
    
