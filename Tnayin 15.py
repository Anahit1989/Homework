file1=open("file.txt","w")
num=int(input("Please enter the number of elements in your file: "))
for i in range(num):
	element=input("Please input your element: ")
	file1.write(element+"\n")
My_list=[]
file1=open("file.txt","r")
for j in file1:
	length=len(j)		
	My_list.append(length)
if len(j)==max(My_list):
	print(j)

file=open("file1.txt", "r")
number_of_lines=0
for i in file:
	if i:
		number_of_lines+=1
print(number_of_lines)

file2=open("file2.txt","w")
file3=open("file3.txt", "r")
My_list=[]
num=int(input("Please enter the number of items in your list: "))
for i in range(num):
	item=input("Please enter your list intem: ")
	My_list.append(item)
for j in My_list:
	file3=open("file3.txt", "a")
	file3.write(j+"\n")
print(file3)

file4=open("file5.txt", "w")
file=open("file1.txt", "r")
for i in file:
	file4.write(i+"\n")
print(file4)

def even_numbers():
	my_new_list=[]
	num=int(input("Please enter the number of your item: "))
	for i in range(num):
		item=int(input("Please enter the item of your list: "))
		my_new_list.append(item)
	if item%2==False:
		print(item)
					
even_numbers()