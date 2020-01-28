"""

@author Jorge Segade 2º DAM

"""
nombreClase = input("introduce el nombre para la clase: ")
nombreClase = nombreClase.capitalize()
numAtt = int(input("introduce el número de atributos: "))
listaAtt = []
for i in range(1, numAtt + 1):
    listaAtt.append(input("introduce atributo " + str(i) + ": ").strip())

archivo = open(nombreClase + ".py", "w")

archivo.write("class " + nombreClase + ":\n\t")
archivo.write("def __init__(self")
for l in listaAtt:
    archivo.write(", " + l);

archivo.write("):\n")

for l in listaAtt:
    archivo.write("\t\tself.__" + l + " = " + l + "\n")

for l in listaAtt:
    # getter
    archivo.write("\t@property\n")
    archivo.write("\tdef " + l + "(self):\n")
    archivo.write("\t\treturn self.__" + l + "\n\n")
    # setter
    archivo.write("\t@" + l + ".setter\n")
    archivo.write("\tdef " + l + "(self, nuevo):\n")
    archivo.write("\t\tself.__" + l + " = nuevo\n\n")

# str()
archivo.write("\tdef __str__(self):\n\t\treturn ")

cont = 0
for l in listaAtt:
    if cont < len(listaAtt) - 1:
        archivo.write("\" " + l + " \"" + " + str(self.__" + l + ") + ")
        cont += 1
    else:
        archivo.write("\" " + l + " \"" + " + str(self.__" + l + ")")

archivo.close()
