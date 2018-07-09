# creando una funcion
def ThisFunctions():
	print("Esta es una funcion")

# llamando a la funcion
ThisFunctions()

# funcion con 2 parametros
def function2(name, lastname):
	print(name, lastname)

# llamada con KeysWord
function2(lastname = 'Mota', name='Erik')

# funcion con parametros arbitrarios
def functionParams(var1, *var2):
	print(var1)

	for value in var2:
		print(value)

functionParams(1, 'valor', 'valor2', 'valor3')

# funcion con parametros  de doble arbitraje
def functionParams2(**var):
	for key in var:
		print("Key -> (", key ,") value -> (",  var[key] ,")")

functionParams2(name = "Erik",lastname = "Mota")

def foo(num1, num2):
	if num1 > num2:
		print("El primer numero  es mayor que el segundo numero ")
	elif num1 == num2:
		print("Son identicos....")
	else:
		print("El segundo es mayor que el primer numero")


my_values = [2,3]
foo(*my_values)

my_values2 = { "num1" : 12, "num2": 10}
foo(**my_values2)