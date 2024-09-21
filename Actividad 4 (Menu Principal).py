#Menu principal
libros_disponibles = { #Diccionario para almacenar la información
    "001": {"titulo": "Cien Años de Soledad", "vendidos": 10},
    "002": {"titulo": "Don Quijote", "vendidos": 5},
    "003": {"titulo": "El Principito", "vendidos": 8},
    "004": {"titulo": "Los Juegos del Hambre", "vendidos": 4},
    "005": {"titulo": "En Llamas", "vendidos": 2},
    "006": {"titulo": "Sinsajo", "vendidos": 3},
    "007": {"titulo": "Los Juegos del Hambre: Balada de pajaros cantores y serpientes", "vendidos": 1},
    "008": {"titulo": "Maze runner: Corer o morir", "vendidos": 11},
    "009": {"titulo": "Maze runner: Cura mortal", "vendidos": 12},
    "010": {"titulo": "Flores en el atico", "vendidos": 0}
}
libros_vendidos = {}
clientes = {}

def menu_principal():
    print("\nMenú principal:")
    print("1. Comprar libro")
    print("2. Regresar libro")
    print("3. Registrar libro")
    print("4. Libros vendidos")
    print("5. Libros más vendidos")
    print("6. Buscar libro")
    print("7. Salir")

#Función para la compra de los libros
def comprar_libro():
    cliente = input("Nombre y apellido del cliente: ")
    cantidad_libros = int(input("Número de libros a comprar: "))

    for i in range(cantidad_libros):
        libro_id = input(f"Introduzca el número de identificación del libro {i+1}: ")
        if libro_id in libros_disponibles:
            libro = libros_disponibles[libro_id]
            libro["vendidos"] += 1  # Incrementamos la cantidad vendida
            libros_vendidos[libro_id] = libros_vendidos.get(libro_id, 0) + 1
            print(f"Libro '{libro['titulo']}' comprado con éxito.")
        else:
            print(f"El libro con ID {libro_id} no está disponible.")
    
    clientes[cliente] = cantidad_libros
    print(f"Compra realizada para {cliente}.")
    print()

#Función para poder regresar libros
def regresar_libro():
    cliente = input("Nombre y apellido del cliente: ")
    libro_id = input("Introduzca el número de identificación del libro a regresar: ")

    if cliente in clientes and libro_id in libros_vendidos:
        libros_vendidos[libro_id] -= 1 
        print(f"Libro con ID {libro_id} regresado exitosamente por {cliente}.")
    else:
        print("No se encuentra el libro o cliente en el sistema.")
    print()

#Función para poder registrar libros al sistema 
def registrar_libro():
    libro_id = input("Ingrese el número de identificación del libro: ")
    titulo = input("Ingrese el título del libro: ")

    if libro_id not in libros_disponibles:
        libros_disponibles[libro_id] = {"titulo": titulo, "vendidos": 0}
        print(f"Libro '{titulo}' registrado exitosamente.")
    else:
        print("Ese libro ya está registrado en el sistema.")
    print()

#Función para mostrar la cantidad de libros vendidos
def mostrar_libros_vendidos():
    print("\nLibros vendidos:")
    for libro_id, cantidad in libros_vendidos.items():
        titulo = libros_disponibles[libro_id]["titulo"]
        print(f"{titulo} (ID: {libro_id}) - Vendidos: {cantidad}")
    if not libros_vendidos:
        print("No se han vendido libros todavía.")
    print() 

#Función para los que más se han vendido
def libros_mas_vendidos():
    print("\nLibros más vendidos:")
    if libros_vendidos:
        libros_ordenados = sorted(libros_vendidos.items(), key=lambda x: x[1], reverse=True)
        for libro_id, cantidad in libros_ordenados[:3]:  # Mostrar los 3 más vendidos
            titulo = libros_disponibles[libro_id]["titulo"]
            print(f"{titulo} (ID: {libro_id}) - Vendidos: {cantidad}")
    else:
        print("No hay libros vendidos todavía.")

def buscar_libro():
    libro_id = input("Introduzca el número de identificación del libro que desea buscar: ")
    if libro_id in libros_disponibles:
        libro = libros_disponibles[libro_id]
        print(f"Libro encontrado: {libro['titulo']} - Vendidos: {libro['vendidos']}")
    else:
        print("Libro no encontrado.")

while True:
    menu_principal() 
    opcion = input("Selecciona el número de lo que deseas hacer: ")

    if opcion == "1":
        comprar_libro()
    elif opcion == "2":
        regresar_libro()
    elif opcion == "3":
        registrar_libro()
    elif opcion == "4":
        mostrar_libros_vendidos()
    elif opcion == "5":
        libros_mas_vendidos()
    elif opcion == "6":
        buscar_libro()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")