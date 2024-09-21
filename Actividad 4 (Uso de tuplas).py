#Uso de tuplas
libros = ("Cien Años de Soledad", "Don Quijote", "El Principito", "Los Juegos del Hambre", "Sinsajo")

print("El tercer libro en la tupla es:", libros[2])

nuevo_libro_1 = input("Introduce el nombre de un nuevo libro para agregar: ")
nuevo_libro_2 = input("Introduce el nombre de otro libro para agregar: ")

libros_lista = list(libros)
libros_lista.append(nuevo_libro_1)
libros_lista.append(nuevo_libro_2)

libros_lista.sort()
print("\nLista de libros ordenada:")
print(libros_lista)

libros_tupla = tuple(libros_lista)

def sumar_caracteres(tupla_libros):
    total_caracteres = 0
    for libro in tupla_libros:
        total_caracteres += len(libro)
    return total_caracteres


total_caracteres = sumar_caracteres(libros_tupla)
print("\nLa suma total de caracteres en los títulos de los libros es:", total_caracteres)
