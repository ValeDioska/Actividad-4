#Uso de diccionarios
contactos = {
    "Vero": "123456789",
    "Dario": "987654321",
    "Obi-Wan": "456789123",
    "Nusy": "8123727391",
    "Tony": "70845391"
}

nombre = input("Ingresa el nombre del nuevo contacto: ")
telefono = input("Ingresa el número de teléfono del nuevo contacto: ")
contactos[nombre] = telefono

print("Lista de contactos:")
for nombre in contactos:
    print(nombre)

def telefono(contactos, nombre):
    return contactos.get(nombre, "Contacto no encontrado")

nombre_a_buscar = input("Ingresa el nombre del contacto que deseas buscar: ")
telefono_encontrado = telefono(contactos, nombre_a_buscar)
print(f"El número de teléfono de {nombre_a_buscar} es:", telefono_encontrado)
