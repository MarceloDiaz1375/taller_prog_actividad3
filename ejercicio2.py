from ejercicio1 import valor_maximo
from ejercicio1 import ingresar_numero

lista_numeros = []
cantidad = 1
while cantidad <= 10:
    print(f"Numero {cantidad}")
    numero = ingresar_numero()
    lista_numeros.append(numero)
    cantidad += 1

print(f"Lista: {lista_numeros}")

resultado = (valor_maximo(lista_numeros))
print(f"El valor maximo de los diez numeros es: {resultado}")

