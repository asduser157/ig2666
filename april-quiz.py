# Level 0
# asks user for their name
greet = input("What is your first name?\n")
# greets user w/ their name
print("Hello there, %s!" % (greet))

# Level 1
#asks user for desired math function
calc = input("Type '+' for addition, '-' for subtraction, '*' for multiplication, or '/' for division:\n")
#asks user for first number in equation
int num1 = get_int("Enter in the first number:\n")
#asks user for second number in equation
int num2 = get_int("Enter in the second number:\n")
if (calc == "+"):
    print("%i + %i: %i" % (num1, num2,(num1+num2)))


