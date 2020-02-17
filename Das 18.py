class sum_to_sero():

	def __init__(self, n_list,result_list):
		self.n_list=n_list
		self.result_list=result_list
	def get_sero_sum_numbers(self):
		return self.result_list

n_list=[]
result_list=[]
num=int(input("Please enter the number of items in your list: "))
for item in range(num):
	item=int(input("Please enter an arbitrary number: "))
	n_list.append(item)
for j in range(1):
	for i in range(num):
		for k in range(num):
			for m in range(num):
				if n_list[i]+n_list[k]+n_list[m]==0 and i<k<m:
					j=[(n_list[i], n_list[k], n_list[m])]
					result_list.append(j)
result=sum_to_sero(n_list, result_list)
print(result.get_sero_sum_numbers())

class degree():
	def __init__(self,x,n):
		self.x=x
		self.n=n
	def x_by_n(self):
		return self.x**self.n
x=int(input("Please enter an arbitrary number: "))
n=int(input("Please enter an arbitrary number: "))
x_and_n=degree(x,n)
print(x_and_n.x_by_n())

class change_order():
	def __init__(self,word1,word2):
		self.word1=word1
		self.word2=word2
	def change(self):
		return self.word2 +" "+self.word1
word1=input("Please enter a word you like: ")
word2=input("Please enter another word you like: ")
wanted_order=change_order(word1,word2)
print(wanted_order.change())

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

class Rectangle():
	def __init__(self,length,width):
		self.length=length
		self.width=width
	def area(self):
		return self.length*self.width
length=int(input("Please enter the length of rectangle: "))
width=int(input("Please enter the width of rectangle: "))
area_of_rectangle=Rectangle(length,width)
print(area_of_rectangle.area())
