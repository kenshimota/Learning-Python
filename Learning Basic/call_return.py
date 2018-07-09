def funcion():
	return "Hola Mundo"

def llamada_de_retorno(func=""):
	"""Llamada de retorno a nivel global"""
	return globals()[func]()

print(llamada_de_retorno("funcion"))
# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"

print (locals()[nombre_de_la_funcion]())