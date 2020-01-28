# Generador-de-Clases-Python
Genera  la clase .py con: constructor, atributos privados, getters, setters y str()

Ejecutar GeneradorDeClases.py 

la salida por consola:




Introduce el nombre para la clase: persona 

Introduce el número de atributos: 3

Introduce atributo 1: nombre

Introduce atributo 2: apellido

Introduce atributo 3: edad



Se generará una clase .py con esos valores al lado de GeneradorDeClases.py 

La clase generada :
----------------------------------------------------------------


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo):
        self.__apellido = nuevo

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nuevo):
        self.__edad = nuevo

    def __str__(self):
        return " nombre " + str(self.__nombre) + " apellido " + str(self.__apellido) + " edad " + str(self.__edad)
