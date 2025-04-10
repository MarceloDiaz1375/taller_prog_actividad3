productos = [["Licuadora", "Philips", "150.00", "5"],
            ["Heladera", "Dream", "500.00", "10"],
            ["Televisor", "Philips", "1500.00", "0"]
            ]

def mostrar_productos(matriz):
    for lista in matriz:
        print(lista)

def cargar_matriz(nombre, prov, precio, stock):
    productos.append([nombre, prov, precio, stock])

def productos_proveedor(prov):
    encontrado = 0
    for producto in productos:
        if producto[1].lower() == prov:
            print(producto)
            encontrado += 1
    if not encontrado:
        print("Proveedor no encontrado")

def menor_precio():
    menor = productos[0]
    menor_float = float(productos[0][2])
    for producto in productos:
        precio = float(producto[2])
        if precio < menor_float:
            menor = producto
    return menor

def stock_positivo():
    positivos = []
    for producto in productos:
        producto[3] = int(producto[3])
        if producto[3] > 0:
            positivos.append(producto)
    for producto in positivos:
        print(producto)



if __name__ == "__main__":
    
    while True:
        print("\n****** Menu de opciones ******")
        print("1 - Cargar un nuevo producto")
        print("2 - Mostrar productos de un proveedor")
        print("3 - Mostrar todos los productos")
        print("4 - Mostrar el producto con el menor precio")
        print("5 - Mostrar los productos con stock positivo")
        print("0 - Salir")

        opcion = input("\nIngrese el numero de la opcion elegida: ")

        if opcion == "1":
            nombre = input("\nIngrese el nombre del producto: ")
            proveedor = input("Ingrese el proveedor del producto: ")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    break
                except:
                    print("Valor no reconocido, solo ingrese numeros")
            while True:
                try:
                    stock = int(input("Ingrese el stock del producto: "))
                    break
                except:
                    print("Valor no reconocido, solo ingrese numeros enteros")

            precio = str(precio)
            stock = str(stock)

            cargar_matriz(nombre, proveedor, precio, stock)

        elif opcion == "2":
            proveedor = input("\nIngrese el nombre del proveedor: ")
            proveedor = proveedor.lower()
            productos_proveedor(proveedor)

        elif opcion == "3":
            print("\n")
            mostrar_productos(productos)

        elif opcion == "4":
            print("\nEl producto con el menor precio es:")
            print(menor_precio())

        elif opcion == "5":
            print("\nProductos con stock positivo:")
            print(stock_positivo())

        
        elif opcion == "0":
            break

        else:
            print("\nOpcion incorrecta")