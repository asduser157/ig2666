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
# while trigger is not activated, run this code:
while (correct == False):
    # have the user guess
    guess = int(input("Type your guess here:\n"))
    #if guess is too high, tell user to guess lower
    if (guess > rand):
        toohigh = int(input("Guess lower! Type here:\n"))
    #if guess is too low, tell user to guess higher
    elif (guess < rand):
        toolow = int(input("Guess higher! Type here:\n"))
    #if guess is correct, let the user know
    elif (guess == rand):
        print("Correct! The number was %s." % (rand))
        #stop the while loop via a trigger
        correct = True
    else:
        print("ERROR: Please type an integer. Press CTRL+C to rerun program and try again.")


# Level 3
# player1's guess
player1 = input("PLAYER 1- Type in 'r' for rock, 'p' for paper, or 's' for scissors:\n")
# confirmation
print("PLAYER 1- Your move has been recorded.\n\n\n\n\n\n\n\n\n\n\n")
# player2's guess
player2 = input("PLAYER 2- Type in 'r' for rock, 'p' for paper, or 's' for scissors:\n")
# confirmation
print("PLAYER 2- Your move has been recorded.\n\n\n\n\n\n\n\n\n\n\n")
# checking outcome...
if (player1 == "r" & player2 == "s"):
    print("Rock beats scissors! PLAYER 1 wins!")
elif (player1 == "p" & player2 == "s"):
    print("Scissors beats paper! PLAYER 2 wins!")
elif (player1 == "s" & player2 == "s"):
    print("Scissors ties scissors! It's a draw!")
elif (player1 == "r" & player2 == "p"):
    print("Paper beats rock! PLAYER 2 wins!")
elif (player1 == "s" & player2 == "p"):
    print("Scissors beats paper! PLAYER 1 wins!")
elif (player1 == "p" & player2 == "p"):
    print("Paper ties paper! It's a draw!")
elif (player1 == "r" & player2 == "r"):
    print("Rock ties rock! It's a draw!")
elif (player1 == "p" & player2 == "r"):
    print("Paper beats rock! PLAYER 1 wins!")
elif (player1 == "s" & player2 == "r"):
    print("Rock beats scissors! PLAYER 2 wins!")
# making sure that type is correct
else:
    print("ERROR: Please ensure both players have only type 'r', 's', or 'p'. Press CTRL+C to rerun program and try again.")





