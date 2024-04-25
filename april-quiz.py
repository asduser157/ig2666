#imports the random library
import random
# Level 0
# asks user for their name
greet = input("What is your first name?\n")
# greets user w/ their name
print("Hello there, %s!" % (greet))

# Level 1
# asks user for desired math function
calc = input("Type '+' for addition, '-' for subtraction, '*' for multiplication, or '/' for division:\n")
# asks user for first number in equation
num1 = int(input("Enter in the first number:\n"))
# asks user for second number in equation
num2 = int(input("Enter in the second number:\n"))
# adds two numbers if addition is selected
if (calc == "+"):
    print("%i+%i = %i" % (num1, num2,(num1+num2)))
# subtracts two numbers if addition is selected
elif (calc == "-"):
    print("%i-%i = %i" % (num1, num2,(num1-num2)))
# multiplies two numbers if multiplication is selected
elif (calc == "*"):
    print("%i*%i = %i" % (num1, num2,(num1*num2)))
# divides two numbers if division is selected
elif (calc == "/"):
    print("%i/%i = %i" % (num1, num2,(num1/num2)))
# gives user instructions if user mistake is made
else:
    print("Incorrect math function. Please press CTRL+C to rerun program and try again.")

# Level 2
# sets the random number
rand = random.randint(1,20)
# sets a trigger
correct = False
print("The computer has randomly selected a number between 1 and 20. Guess it correctly to move forward.\n")
#while trigger is not activated, run this code:
while (correct == False):
    guess = int(input("Type your guess here:\n"))
    if (guess > rand):
        toohigh = int(input("Guess lower! Type here:\n"))
    if (guess < rand):
        toolow = int(input("Guess higher! Type here:\n"))
    if (guess == rand):
        print("Correct! The number was %s." % (rand))
        correct = True





