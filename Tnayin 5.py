name=input("Enter your name: ")
age=input("Enter your age: ")
age=int(age)
current_year=input("Enter current_year: ")
current_year=int(current_year)
target_year=current_year+(100-age)
print("You will turn 100 years old in " + str(target_year)+ ".")
Number1=input("Enter the first unmber: ")
Number1=int(Number1)
Number2=input("Enter the seconf number: ")
Number2=int(Number2)
Number3=input("Enter the third number: ")
Number3=int(Number3)
print(Number1==Number2==Number3)
print(Number1==Number2 or Number1==Number3 or Number2==Number3)
first_number=input("Enter an arbitrary number: ")
first_number=int(first_number)
second_number=input("Enter an arbitrary number: ")
second_number=int(second_number)
sum_of_two_nmbers=first_number+second_number
print(sum_of_two_nmbers>5, sum_of_two_nmbers==5, sum_of_two_nmbers<5)
passing_mark=35
your_mark=input("Enter your mark: ")
your_mark=int(your_mark)
print(your_mark>passing_mark)