# applicant_info={"Name": "Lily", "Surname": "Melqonyan"}
# applicant_info["Age"] = 19
# applicant_info["Citizenship"] = "RA"
# print(applicant_info)

dic1={"Name": "Gohar", "Surname":"Meliqyan"}
dic2={"Age": 25, "Weight":55}
dic3={"Hight": 170, "Race": "Armenoid"}
dic4={**dic1,**dic2,**dic3}
print(dic4)

About_Gohar={"Name": "Gohar", "Surname":"Meliqyan","Age": 25, "Weight":55}
if "Age" in About_Gohar:
	print("The key is in the dictionary.")
else:
	print("There is no such key in the dictionary.")

About_You={}
name=input("Please enter your name: ")
surname=input("Please enter your surname: ")
age=input("Please enter your age: ")
About_You["Name"]=name
About_You["Surname"]=surname
About_You["Age"]=age
print(About_You)

dict1={"a":1000, "b":1500, "c":500, "d":0}
for kv in dict1.items():
	if kv[1]==max(dict1.values()):
		print(kv[0])

my_string="soRry"
my_dict={}
my_dict[my_string[0]]=1
my_dict[my_string[1]]=1
my_dict[my_string[2]]=1
my_dict[my_string[3]]=1
my_dict[my_string[4]]=1
print(my_dict)




