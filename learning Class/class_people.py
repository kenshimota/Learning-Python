class People():

	name = "" 

	# obtiene el nombre de la persona
	def getName(self):
		return self.name

	# funcion que agrega el nombre de la persona
	def setName(self, str = ""):
		if str != "":
			self.name = str

	# fabrica el input para obtene el nombre
	def inputName(self):
		name_tmp = input("Ingrese su nombre: ")
		self.setName(name_tmp)


people1 = People()
people1.inputName()
print( people1.getName() )