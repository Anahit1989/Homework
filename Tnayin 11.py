while True:
	user_input=input("Please enter a sentence: ")
	if user_input.endswith(" "):
		print("Your sentence ends with space, please correct it!")
	else:
		user_input.count(" ")
		number_of_words = user_input.count(" ") + 1
		print("Sum of words in the sentence: ", number_of_words)
		break

user_phone_num=input("Please enter your phone number: ")
try:
	if user_phone_num[0:3] == "091" or user_phone_num[0:3] =="099" or user_phone_num[0:3]=="041":
		print("Your operator is Beeline")
	elif user_phone_num[0:3]=="093" or  user_phone_num[0:3]=="094" or user_phone_num[0:3]=="098" or user_phone_num[0:3] =="077":
		print("Your operator is VivaCell")
	else:
		print("Your operator is Ucom")
except:
	print("Error")


try:
	user_input=int(input("Please enter the year of your birth: "))
	part_of_10millennium=10000/user_input
		
	# print("You was born in "+number_of_centuries+" part of 10000 milleenium")
	print("You was born in "+part_of_10millennium+" century")
except TypeError:
	print("You have a concatenation error. Your inputs have different types.")

except ZeroDivisionError:
	print("You can't devide the number on 0.")

except ValueError:
	print("You have enterd wrong value. Enter an intiger!")

except NameError:
	print("There is no a variable with such name.")