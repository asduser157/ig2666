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
    print("%i + %i: %i" % (num1, num2,(num1+num2)))
# subtracts two numbers if addition is selected
elif (calc == "-"):
    print("%i - %i: %i" % (num1, num2,(num1-num2)))
# multiplies two numbers if multiplication is selected
elif (calc == "*"):
    print("%i * %i: %i" % (num1, num2,(num1*num2)))
# divided two numbers if division is selected
elif (calc == "/"):
    print("%i / %i: %i" % (num1, num2,(num1/num2)))
#gives user instructions if user mistake is made
else:
    print("Incorrect math function. Please press CTRL+C to rerun program and try again.")

# Level 2



