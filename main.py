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
question = input("What do you want?\n 1 - Add\n 2 - Sub\n 3 - Mult\n 4 - Div\n 5 - Percentage\n 6 - Square Root\n  Insert number: ")
# Set the firstValue as an int
int_first = int(firstValue)

# If the operation is the square root, it doesn't ask for a second number, otherwise it asks for it
if  question == '6':
    secondValue = int(int_first)
else:
    secondValue = input("Second Value:")
# Set the secondValue as an int
int_second = int(secondValue)
# If the user wants to do a certain operation it follows with the assigned operation, otherwise it inputs an error
if question == '1':
    print(f"The result of your addition is: {int_first + int_second}")
elif question == '2':
    print(f"The result of your subtraction is: {int_first - int_second}")
elif question == '3':
    print(f"The result of your multiplication is: {int_first * int_second}")
elif question == '4':
    print(f"The result of your division is: {int_first / int_second}")
elif question == '5':
    print(f"The percentage of {int_first}% of {int_second} is {int_first / 100 * int_second}")
elif question == '6':
    print(f"The result of your square root is: {int_first * int_second}")
else:
    print("Do not compute")