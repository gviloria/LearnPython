# Odd or Even
number = int(input("Please enter a number: "))
divide = int(input("Please enter a number to divide the previous number by: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
if number % 4 == 0:
    print("The number is also divisible by 4.")
if number % divide == 0:
    print("The number is also divisible by '" + str(divide) + "'.")
