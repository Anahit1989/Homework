class sum_to_target():

	def __init__(self, n_list):
		self.n_list=n_list

n_list=[]
num=int(input("Please enter the number of items in your list: "))
for item in range(num):
	item=int(input("Please enter an arbitrary number: "))
	n_list.append(item)
for j in range(num):
	for i in range(num):
		if n_list[j]+n_list[i]==50 and j<i:
			print(j,i)

class Person():
	def __init__(self, name, surname, age):
		self.name = name
		self.surname=surname
		self.age=age

Member1=Person("Patric", "Jobs", 55)
print(type(Member1).__name__)
print(Member1.__class__.__name__)

class Point3D():
	def __init__(self, x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point=Point3D(1,2,3)
print(my_point)