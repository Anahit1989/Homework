user_input=input("Enter an arbitrary word: ")
first_char = user_input[0]
sample=user_input[1:len(user_input)]
sample.replace(first_char, "$")
sample=sample.replace(first_char, "$")
print(first_char+sample)


user_input=input("Please enter a word: ")
if len(user_input)>=3:
	if user_input.endswith("ing"):
		print(user_input+"ly")
	else:
		print(user_input+"ing")
else:
	print(user_input)


while True:
	user_input=input("Please enter a sentence with word poor: ")
	if "not" in user_input and "poor" in user_input:
		if user_input.index("not") < user_input.index("poor"):
			user_input.replace(user_input[user_input.index("not"):(user_input.index("poor")+4)], "good")
			user_input=user_input.replace(user_input[user_input.index("not"):user_input.index("poor")+4], "good")
			print(user_input)
		else:
			print(user_input)
		break
	elif "poor" in user_input:
		print(user_input)
		break
	else:
		print("Your sentence doesn't contain the word poor. Please enter a sentence with word poor!")	

			
		
			
		
		
			

	