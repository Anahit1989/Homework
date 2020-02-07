# My_tuple=((3,4,5),(0,1,2),(6,7,8))
# print(My_tuple[0])
# print(My_tuple[0][0])
# My_list=[(0,1,2),3,4]
# print(My_list[0])
# stock_list=["apple","pear", "peach", "orange"]
# wish_list=[]
# number=int(input("How many items do you want you buy? "))
# for n in range(number):
# 	item=input("Please enter your wished item: ")
# 	if item in stock_list: 
# 		wish_list.append(item)
# print(wish_list)

user_items_number=int(input("Input the number of items you want to buy: "))
user_prefered_items=[]
market_stock=["Ice-cream", "Juice","Apple"]
user_avaliable_items = []

for i in range(user_items_number):
	item =input("enter item name you want to buy: ")
	user_prefered_items.append(item)
for item in user_prefered_items:
	if item in market_stock:
		user_avaliable_items.append(item)
print(user_avaliable_items)
		

