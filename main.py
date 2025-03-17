# Set the line Width
design = 60
print("%"*design)
print("%%"+"Calculator".center(56)+"%%")
print("%"*design)
#Ask for first Value
firstValue = input("First Value: ")
# Set the second value as 0 to be updated later
secondValue = 0
# Asks what operation the user wants
question = input("What do you want?\n "
                 "1 - Add\n "
                 "2 - Sub\n "
                 "3 - Mult\n "
                 "4 - Div\n "
                 "5 - Percentage\n "
                 "6 - Square Root\n  "
                 "Insert number: ")
# Set the firstValue as an int
int_first = float(firstValue)

# If the operation is the square root, it doesn't ask for a second number, otherwise it asks for it
if  question == '6':
    secondValue = float(int_first)
else:
    secondValue = input("Second Value:")
# Set the secondValue as an int
int_second = float(secondValue)
# If the user wants to do a certain operation it follows with the assigned operation, otherwise it inputs an error
if question == '1':
    print(f"The result of your addition is: {round(int_first) + round(int_second)}")
elif question == '2':
    print(f"The result of your subtraction is: {round(int_first) - round(int_second)}")
elif question == '3':
    print(f"The result of your multiplication is: {round(int_first) * round(int_second)}")
elif question == '4' and int_second == 0:
    print("Cannot divide by 0")
elif question == '4':
    print(f"The result of your division is: {round(int_first) / round(int_second)}")
elif question == '5':
    print(f"The percentage of {round(int_first)}% of {round(int_second)} is {round(int_first) / 100 * round(int_second)}")
elif question == '6':
    print(f"The result of your square root is: {round(int_first) * round(int_second)}")
else:
    print("Do not compute")