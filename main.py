print("Welcome to this calculator")
print('''Press 1 for addition
Press 2 for subtraction
Press 3 for multiplication
Press 4 for division
Press 5 for getting the remainder of division''')

choice = int(input("Your age"))
num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))

add = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2
remainder = num1 % num2

if choice == 1:
    print("addition of {} + {} = {}".format(num1, num2, add))

elif choice == 2:
    print("subtraction of {} - {} = {}".format(num1, num2, subtraction))

elif choice == 3:
    print("multiplication of {} × {} = {}".format(num1, num2, multiplication))

elif choice == 4:
    print("division of {} ÷ {} = {}".format(num1, num2, division))

elif choice == 5:
    print("remainder of {} and {} is {}".format(num1, num2, remainder))

else:
    print("Please enter a valid input")
