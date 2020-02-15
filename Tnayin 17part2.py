class String:
	def __init__(self, string):
		self.string = string
	def get_String(self):
		return self.string
	def print_String(self):
		print(string.upper())

string=input("Enter a string:")
my_string=String(string)
print(my_string.get_String())
my_string.print_String()	


class Vehical:
	def __init__(self, name, color, model, price):
		self.name=name
		self.color=color
		self.model=model
		self.price=price
car1=Vehical("Fer", "red", "convertible", 60000)
car2=Vehical("Jump", "blue", "van", 10000)
print(car1.name)
print(car2.name)
				

