# a program that creates a class, object(s) of that class and shows some attributes and methods of those object(s).

# creating a class
class Car:
	def __init__(self, name, manuf, color, yr, cc):
		self.name = name
		self.manuf = manuf
		self.color = color
		self.yr = yr
		self.cc = cc

	def start(self):
		print("Starting the engine...")

	def drive(self):
		print("Driving..")

	def brake(self):
		print("Braked!")

	def turn(self):
		print("Turning..")

	def changeGear(self):
		print("Changing gear..")

# creating Car objects
car1 = Car("Mercedes-Benz SLS AMG", "Mercedes-Benz", "Grey", 2010, 6208)
car2 = Car("BMW 8-series (G14)", "BMW", "Red", 2018, "N/A")

# showing the attributes and behavior of Car objects
print("Car details")
print("-----------")
print("Car name:", car1.name)
print("Car manufacturer:", car1.manuf)
print("Car color:", car1.color)
print("Invention Year:", car1.yr)
print("cc:", car1.cc)
car1.start()
car1.drive()
print("Car name:", car2.name)
print("Car manufacturer:", car2.manuf)
print("Car color:", car2.color)
print("Invention Year:", car2.yr)
print("cc:", car2.cc)
car2.start()
car2.drive()
car2.changeGear()
