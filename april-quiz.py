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
guess = int(input("Type your guess here:\n"))
while (correct == False):
    # have the user guess
    #if guess is too high, tell user to guess lower
    if (guess > rand):
        guess = int(input("Guess lower! Type here:\n"))
    #if guess is too low, tell user to guess higher
    elif (guess < rand):
        guess = int(input("Guess higher! Type here:\n"))
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
print("PLAYER 1- Your move has been recorded.\n\n")
# player2's guess (computer)
array1 = ["r", "p", "s"]
player2 = random.choice(array1)
# checking outcome...
if (player1 == "r" and player2 == "s"):
    print("Rock beats scissors! You win!")
elif (player1 == "p" and player2 == "s"):
    print("Scissors beats paper! You lose!")
elif (player1 == "s" and player2 == "s"):
    print("Scissors ties scissors! It's a draw!")
elif (player1 == "r" and player2 == "p"):
    print("Paper beats rock! You lose!")
elif (player1 == "s" and player2 == "p"):
    print("Scissors beats paper! You win!")
elif (player1 == "p" and player2 == "p"):
    print("Paper ties paper! It's a draw!")
elif (player1 == "r" and player2 == "r"):
    print("Rock ties rock! It's a draw!")
elif (player1 == "p" and player2 == "r"):
    print("Paper beats rock! You win!")
elif (player1 == "s" and player2 == "r"):
    print("Rock beats scissors! You lose!")
# making sure that type is correct
else:
    print("ERROR: Please ensure you only type 'r', 's', or 'p'. Press CTRL+C to rerun program and try again.")

# Level 4
# first question
quiz1 = input("Donald Duck's middle name is:\n")
# score variable
score = 0
# answer checker and score tracker
if (quiz1 == "Fauntleroy" or quiz1 == "fauntleroy"):
    print("Correct!\n")
    score = (score + 1)
else:
    print("Wrong! The correct answer is: Fauntleroy\n")
    score = (score + 0)
# relaying current score
print("Your current score is: %i" % (score))
# second question
quiz2 = input("The largest species of rodent in the world is a/an:\n")
# answer checker and score tracker
if (quiz2 == "Capybara" or quiz2 == "capybara"):
    print("\nCorrect!")
    score = (score + 1)
else:
    print("\nWrong! The correct answer is: capybara\n")
    score = (score + 0)
# relaying current score again
print("Your current score is: %i" % (score))
# third question
quiz3 = input("A polar bear's fur is this color:\n")
# answer checker and score tracker
if (quiz3 == "Clear" or quiz3 == "clear"):
    print("\nCorrect!")
    score = (score + 1)
else:
    print("\nWrong! The correct answer is: clear | (It appears white because it reflects off the snow)")
    score = (score + 0)
# relaying score once again
print("\nYour current score is: %i" % (score))
quiz4 = input("\nThe fastest animal in the world is a/an:\n")
# answer checker and score tracker
if (quiz4 == "Peregrine Falcon" or quiz4 == "peregrine falcon" or quiz4 == "Peregrine falcon" or quiz4 == "peregrine Falcon"):
    print("Correct!")
    score = (score + 1)
else:
    print("\nWrong! The correct answer is: peregrine falcon")
    score = (score + 0)
# putting score in a percentage
percent = (score/4)*100
score = (score + 0)
# relaying final score
print("\nYour final score is: %i/4 (%i%)" % (score, percent))
#END OF PROGRAM

