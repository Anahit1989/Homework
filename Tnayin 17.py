FILE=open("bank_file.txt","a")
class BankAccount:
	def __init__(self, name, surname, email, balance=0):
		self.name = name
		self.surname = surname
		self.email = email
		self.balance = balance

	def get_balance(self):
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		# self.get_balance()
		return self.get_balance()

	def with_drow(self, amount):
		self.balance -= amount
		# self.get_balance()
		return self.get_balance()

def create_instance():
	global user_dict
	user_dict = {}
	name = input("Enter your name: ")
	surname = input("Enter your surname: ")
	email = input("Enter your email: ")
	user_dict[name] = BankAccount(name, surname, email)
	FILE.write("Name: "+name+", Surname: "+surname+", Email: "+email+"\n")

def get_balance():
	name = input("Enter your name: ")
	z=user_dict[name].get_balance()
	print(z)
	FILE.write("Your inisial balance is: "+str(z)+"AMD"+"\n")
	
def put_deposit():
	name = input("Enter your name: ")
	amount=int(input("Enter the sum: "))
	y=user_dict[name].deposit(amount)
	print(y)
	FILE.write("You deposited: " + str(amount)+"AMD"+"\n"+"Your final balanc is: "+str(y)+"AMD"+"\n")
	
def get_money():
	name = input("Enter your name: ")
	amount=int(input("Enter the sum: "))
	x=user_dict[name].with_drow(amount)
	print(x)
	FILE.write("You withdrawed: "+str(amount)+"AMD"+"\n"+"Your final balanc is: "+str(x)+"AMD"+"\n")
	
while True:
	print("1) Create account: ")
	print("2) Deposit: ")
	print("3) Withdraw: ")
	print("4) Check Balance: ")
	print("5) Exit Programm: ")
	user_choice = input("Choose one of the options: ")
	if user_choice == "1":
		create_instance()
	elif user_choice=="2":
		put_deposit()	
	elif user_choice == "3":
		get_money()	
	elif user_choice == "4":
		get_balance()	
	else:
		print("Thank you for choosing our Bank. Have a good day!")
		break
	

FILE.close()

