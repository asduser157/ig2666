import time
import os
import sys
import platform


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clearScreen()
password = typingInput("Enter in the passcode to skip the credits.\n")

if password != "Harold":
    clearScreen()

    typingPrint('DASHELL  HANBERG')
    print('')
    typingPrint('   ~presents~    ')
    time.sleep(3)
    clearScreen()

    typingPrint('      ~Along with~    ')
    print('')
    print('')
    typingPrint('     ISAAC R. GRANDY      ')

    time.sleep(3)
    clearScreen()

    typingPrint(' A Crescent Moon Games ')
    print('')
    typingPrint('       Creation       ')
    time.sleep(3)
    clearScreen()

    typingPrint("          With           ")
    print('')
    typingPrint("Symmetrical Space Capybara")
    print('')
    typingPrint("       Productions       ")

    time.sleep(3)
    clearScreen()

    typingPrint('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    typingPrint(' |=====================|')
    print('')
    typingPrint('  |Dragons of Darkness|')
    print('')
    typingPrint(' |=====================|')
    print('')
    typingPrint('~~~~~~~~~~~~~~~~~~~~~~~~~')
    time.sleep(3.75)
    clearScreen()
    name = typingInput('''What is your name?
''')
    typingPrint('Welcome to Terronis, %s.' %(name))
    time.sleep(3)
    clearScreen()
    typingPrint("CHAPTER ONE")
    print('')
    time.sleep(2)
    typingPrint("It is a peaceful night in Terronis.")
    time.sleep(0.5)
    print('')
typingPrint("You walk the streets of town enjoying a cup of honeydrink from the local tavern.")
time.sleep(0.5)
print('')
typingPrint("When you left the tavern, the streets were packed.")
time.sleep(0.5)
typingPrint(" By the time you finish your drink, the streets are empty.")
time.sleep(0.5)
print('')
typingPrint("You toss your cup away.")
time.sleep(0.5)
typingPrint(" Seconds later you hear the cup thud and bounce on the dirt...")
time.sleep(0.5)
print('')
typingPrint("and an explosion shakes the village.")
time.sleep(0.5)
typingPrint(" You turn around, wondering what your cup could have hit to have caused such an explosion.")
time.sleep(0.5)
print('')
typingPrint("That's when you see it.")
time.sleep(0.5)
typingPrint(" A massive purple dragon, flying above the village.")
time.sleep(0.5)
typingPrint(" It opens it spacious mouth and a fireball billows forth.")
time.sleep(0.5)
print('')
typingPrint("It explodes upon impact, obliterating three entire houses.")
time.sleep(0.5)
typingPrint(" The wind created from the explosion ruffles your hair.")
dragon_attack = typingInput(''' Do you...
1) run away
2) stand still in shock
3) seek shelter in the nearest building

- ''')
if dragon_attack == '2':
    typingPrint("As everyone else runs away, you stand there, frozen with fear.")
    time.sleep(0.5)
    typingPrint(" The dragon sees you as an easy target.")
    time.sleep(0.5)
    print('')
    typingPrint("He dives towards you... ")
    time.sleep(0.5)
    typingPrint("... and disintegrates you with his fireball breath.")
    print('''

''')
    typingPrint("GAME OVER")
    print('')
elif dragon_attack == '3':
    print('')
elif dragon_attack == '1':
    print('')
    typingPrint("The entire village is awake now and running around.")
    time.sleep(0.5)
    typingPrint(" You run with them, sharing a common goal with everyone else:")
    time.sleep(0.5)
    print('')
    typingPrint("get as far away as possible.")
    time.sleep(0.5)
    typingPrint(" You succeed for a while until the dragon lands a few hundred feet in front of you.")
    time.sleep(0.5)
    print('')
    typingPrint(
        "A large burly man yells and accidentally knocks you off your feet into the doorway of a nearby building.")
    time.sleep(0.5)
    print('')
    typingPrint("Instead of landing on wooden things, you land on metal.")
    time.sleep(0.5)
    typingPrint(" As you pick yourself up, you realize that the dragon unwittingly")
    print('')
    typingPrint("put you in the best location in the entire village.")
    time.sleep(0.5)
    typingPrint(" You are in the armory.")
    time.sleep(0.5)
    print('')
    typingPrint("You pick yourself up and look around.")
    time.sleep(0.5)
    typingPrint(" There is everything here.")
    time.sleep(0.5)
    print('')
    typingPrint("Swords, axes, spears, shields, armor, bows and crossbows, you name it, it's there.")
    time.sleep(0.5)
    print('')
    typingPrint("You grab a spear, peek outside at the dragon, then hurl it.")
    time.sleep(0.5)
    print('')
    typingPrint("Once you are finished vomiting, you wipe your mouth on your sleeve.")
    time.sleep(0.5)
    print('')
    typingPrint("The dragon had been enjoying a meal of cow and human innards mixed together.")
    time.sleep(0.5)
    print('')
    typingPrint("You heft the spear once more and throw it, pouring all your arm's strength into the shot.")
    time.sleep(0.5)
    print('')
    typingPrint("The spear plunges into the the dragon inbetween it's shoulder and wing joint.")
    time.sleep(0.5)
    print('')
    typingPrint("You hurry back into the armory as the dragon roars in outrage.")
    time.sleep(0.5)
    typingPrint(" The dragon roars again.")
    time.sleep(0.5)
    typingPrint(" Then, to your suprise,")
    print('')
    typingPrint(" the dragon begins speaking.")
    time.sleep(0.5)
    print('')
    typingPrint(
        "'To the brave little squirt that just stabbed me, I would Be much obliged if you would come and face me.'")
    time.sleep(0.5)
    print('')
    typingPrint("'No one can go injure me and get away with it.'")
    time.sleep(0.5)
    typingPrint("'Don't you agree?'")
