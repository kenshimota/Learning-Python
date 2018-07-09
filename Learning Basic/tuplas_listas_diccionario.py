"""
########################
		TUPLAS

description: es un tipo de
variables que contiene una
serie de datos inmutables  """

my_tupla = ('Erik', 'de', 'Jesus', 'Mota', 'Galindo')

print(my_tupla[0])   # Accediendo a un solo dato de la tupla
print(my_tupla[0:5]) # Accediendo desde el dato 0 hasta el 5
print(my_tupla[:3])  # Accedera a los datos que 

"""
########################
		LISTAS

description: Una lista es similar a 
una tupla con la diferencia fundamental 
de que permite modificar los datos una 
vez creados """

my_list = ['primer valor',2,3.00]

print(my_list[0])   # Accediendo a un solo dato de la lista

# cambiando de valor
my_list[0] = "Cambio de valor"
print(my_list[0])

print(my_list[0:3]) # Accediendo desde el dato 0 hasta el 2 omitendo la 3
print(my_list[:3])  # Accedera a los datos que este desde la posicion 0 hasta el 2

# estas listas tambien permiten agregar valores a
# final de la lista

my_list.append(12)

print(my_list[3])


"""
########################
	  DICCIONARIO

description: Mientras que a las listas 
y tuplas se accede solo y únicamente por 
un número de índice, los diccionarios permiten
utilizar un keys para declarar y acceder a 
un valor """

mi_diccionario = {'clave_1': 1, 'clave_2': 2, 'clave_7': 7}

print(mi_diccionario['clave_2']) # Salida: valor_2

del(mi_diccionario['clave_2']) # permite eliminar cualquier keys

# tambien permite cambiar el valor de uno de los keys
mi_diccionario['clave_1'] = 3
print(mi_diccionario)
