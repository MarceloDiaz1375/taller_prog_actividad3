pacientes = [
    "Morales Manuel",
    "Juan Perez",
    "Soledad Diaz"
]

def agregar_paciente(paciente):
    pacientes.append(paciente)

def agregar_paciente_urgente(paciente):
    pacientes.insert(0, paciente)

def atender_paciente():
    del pacientes[0]

def mostrar_pacientes():
    cont = 0
    for paciente in pacientes:
        cont += 1
        print(f"{cont} - {paciente}")

if __name__ == "__main__":
    
    while True:
        print("\n****** Menu de opciones ******")
        print("1 - Ingresar nuevo paciente")
        print("2 - Atender paciente")
        print("3 - Ingresar paciente con urgencia")
        print("4 - Mostrar la lista de pacientes que faltan ser atendidos")
        print("0 - Salir")

        opcion = input("\nIngrese el numero de la opcion elegida: ")

        if opcion == "1":
            nombre = input("\nIngrese el nombre del paciente: ")
            agregar_paciente(nombre)

        elif opcion == "2":
            print(f"Debe pasar el paciente {pacientes[0]}")
            atender_paciente()

        elif opcion == "3":
            nombre = input("\nIngrese el nombre del paciente: ")
            agregar_paciente_urgente(nombre)

        elif opcion == "4":
            print("\nPacientes restantes: ")
            mostrar_pacientes()
        
        elif opcion == "0":
            break

        else:
            print("\nOpcion incorrecta")