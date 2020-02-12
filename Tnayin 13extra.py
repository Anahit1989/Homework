while True:
	try:
		My_num= int(input("Please enter an arbitrary number: "))
		if My_num in range(0,1000):
			print("Your number is in the specified range.")
			break
		else:
			print("Your number is not in the specified range.")
	except:
		print("ValueError. Please enter an intiger!")

My_string=input("Please enter the story of your life. ")
def calculator():
	number_of_uppercase_letters=0
	number_of_lowercase_letters=0
	for i in My_string:
		if i.isupper():
			number_of_uppercase_letters+=1
		if i.islower():
  			number_of_lowercase_letters+=1
	print("The number of uppercase letters in My_string is ",number_of_uppercase_letters," and the number of lowercase letters is ",number_of_lowercase_letters) 

calculator()

num1=int(input("Please enter the number of elements in list1: "))
def unique():
	list1=[]
	list2=[]
	for i in range(num1):
		item1=input("Please enter the item1: ")
		list1.append(item1)	
	for n in list1: 
		if list1.count(n)==1:
			list2.append(n)
	print(list2)
unique()

def print_number():
	while True:
		try:
			x=int(input("Please input a arbitrary number: "))
			y=int(input("Please input a arbitrary number: "))
			if x%x==False and x%y==True:
				print("x is a prime number")
			else:
				print("x is not a prime number")
			break
		except:
			print("ValueError. Please enter an intiger!")

print_number()
		
		

