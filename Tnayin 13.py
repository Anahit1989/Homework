My_list=[]
number=int(input("Please enter the number of items in your list: "))
number_of_items=0
for n in range(number):
	item=input("Enter the name of item: ")
	My_list.append(item)
	if len(item)>=2 and item[0]==item[-1]:
		number_of_items+=1
print(number_of_items)


My_list=[]
if len(My_list):
	print("The list is not empty")
else:
	print("The list is empty")


My_list=["apple", "aba", "abcsde","abc","123456789"]
for i in range(len(My_list)):
	item=My_list[i]
	list_of_lengths=[]
	list_of_lengths.append(len(item))
print(max(list_of_lengths))


list_1=[]
number1=int(input("Please enter the number of items in list1: "))
for n in range(number1):
	item1=input("Enter the item: ")
	list_1.append(item1)
list_2=[]
number2=int(input("Please enter the number of items in list2: "))
for m in range(number2):
	item2=int(input("Enter the item: "))
	list_2.append(item2)
common_item=False
for i in list_1 and list_2:
	print(i)
	common_item=True
	break
if not common_item:
	print("There is no common_item")



