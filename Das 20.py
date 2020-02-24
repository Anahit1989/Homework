# Task 16

# file=open("Lyrics.txt","r")
# num=int(input("Please enter an arbitrary number from 1 to 38: "))
# for i in file:
# 	if int(i[0])==num:
# 		print(i)
# 	elif int(i[0:2])==num:
# 		print(i)

# file.close()

# Task 17

# x={"key1":1,"key2":3,"key3":2}
# y={"Key1":1,"key2":2}

# for k1, v1 in x.items():
# 	for K2, v2 in y.items():
# 		if v1==v2:
# 			print(k1,":",v1) 

# Task 18

text=input("Please enter a word: ")
key=int(input("Please enter an arbitrary number: "))
def CaesarCipher(text, key):
	cipher = ""
	for letter in text:
		shifted=ord(letter)+key
		cipher+=chr(shifted)
	return cipher

print(CaesarCipher(text, key))

