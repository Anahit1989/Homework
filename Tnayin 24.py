# task  1
list1=[10,20,30,40,50]
list2=[]
for i in range(list1[-1], list1[0]-1, -10):
	list2.append(i)
print(list2)


# task 2
list1=list(range(1,100))
list2=list(range(99,0,-1))
for i in list1:
	for j in list2:
		if list1.index(i)==list2.index(j):
			print(i,'-----',j)



# task 3
list1=list(range(0,10))
list2=list(range(0,10))
list3=list(range(0,10))
for i in list1:
	for j in list2:
		for k in list3:
			a=i
			b=j
			c=k
			print(a,b,c)

