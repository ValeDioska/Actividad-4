#Uso de strings
mensaje = "Los Juegos del Hambre es la mejor saga de libros y peliculas"

print("Longitud del mensaje:", len(mensaje))

#Mensaje a mayúsculas
mensaje_mayus = mensaje.upper()
print("Mensaje en mayúsculas:", mensaje_mayus)

#Reemplazar una palabra en el mensaje
mensaje_reemplazado = mensaje.replace("mejor", "más fantastica")
print("Mensaje modificado:", mensaje_reemplazado)

def contar_palabras(texto):
    return len(texto.split())

#Mensaje y mostrar el resultado
cantidad_palabras = contar_palabras(mensaje)
print("El mensaje contiene", cantidad_palabras, "palabras.")
