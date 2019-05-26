class Vehicle:
	"""Base class: Vehicle for all the classes"""
	def __init__(self, name, manuf, color):
		self.name = name
		self.manuf = manuf
		self.color = color

	def drive(self):
		print("Driving", self.manuf, self.name)

	def turn(self, dir):
		print("Turning", self.name, "to", dir)

	def brake(self):
		print(self.name, "is stopping!")

class Car(Vehicle):
	"""Car class as a derived class"""
	def __init__(self, name, manuf, color, yr):
		# super(Vehicle, self).__init__()
		self.name = name
		self.manuf = manuf
		self.color = color
		self.yr = yr
		self.wheels = 4
		print("A new car has been created. Name:", self.name, ".")
		print("It has", self.wheels, "wheels.")
		print("The car was built in", self.yr, ".")

	def changeGear(self, gearName):
		"""Method for changing gear"""
		print(self.name, "is changing gear to", gearName)

if __name__ == '__main__':
	c1 = Car("BMW-SWC2019", "BMW", "Blue", 2019)
	c2 = Car("MB-XCP2018", "Mercedes-Benz", "Black", 2018)

	c1.drive()
	c2.drive()
	c1.turn("left")
	c2.turn("right")
	c1.changeGear("I")
	c2.changeGear("D")
	c1.brake()
	c2.brake()