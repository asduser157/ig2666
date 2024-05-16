import time
import os
import sys
import platform

# Already done and finished. No further edits will be valid.

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


def credits():
    clearScreen()

    typingPrint('DASHELL  HANBERG')
    print('')
    typingPrint('   ~presents~    ')
    time.sleep(3)
    clearScreen()

    typingPrint('      ~Along with~    ')
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
    typingPrint("      Productions      ")

    time.sleep(3)
    clearScreen()

    typingPrint('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    typingPrint(' |====================|')
    print('')
    typingPrint('  |Dragon of Darkness|')
    print('')
    typingPrint(' |====================|')
    print('')
    typingPrint('~~~~~~~~~~~~~~~~~~~~~~~~~')
    time.sleep(3.75)


def Chapterone():
    clearScreen()
    typingPrint("CHAPTER ONE")
    print('')
    typingPrint('''It is a peaceful night in Terronis. You walk the streets of the city enjoying a cup of honeydrink from the local tavern. When you left the tavern, the streets were packed. By the time you finish your drink, the streets are empty. You toss your cup away. Seconds later you hear the cup thud and bounce on the dirt... and an explosion shakes the city. You turn around, wondering what your cup could have hit to have caused such an explosion. That's when you see it. A massive purple dragon, flying above the city. It opens it spacious maw and a fireball billows forth. It explodes upon impact, obliterating three entire houses. The wind created from the explosion ruffles your hair.''')
    dragon_attack = typingInput(''' Do you...
    1) run away
    2) stand still in shock
    3) seek shelter in the nearest building
    - ''')
    if dragon_attack == '2':
        typingPrint('''As everyone else runs away, you stand there, frozen with fear. The dragon sees you as an easy target. It dives towards you... and disintegrates you with it's fireball breath.
GAME OVER''')
    elif dragon_attack == '3':
        typingPrint('''You run into the nearest building where you are immediately stabbed by a frightened child. You die looking down at the amazing craftsmanship of the handle.
GAME OVER''')
    elif dragon_attack == '1':
        typingPrint("The entire city is awake now and running around. You run with them, sharing a common goal with everyone else: get as far away as possible. You succeed for a while until the dragon lands a few hundred feet in front of you. A large burly man yells and accidentally knocks you off your feet through the doorway of a nearby building. Instead of landing on wooden things, you land on metal. As you pick yourself up, you realize that the dragon unwittingly put you in the best location in the entire city. You are in the armory. You pick yourself up and look around. There is everything here. Swords, axes, spears, shields, armor, bows and crossbows, you name it, it's there. You grab a spear and  peek outside at the dragonthen hurl it. Once you are finished vomiting, you wipe your mouth on your sleeve. The dragon had been enjoying a meal of cow and human innards mixed together. You heft the spear once more and throw it, pouring all your arm's strength into the shot. The spear plunges into the the dragon inbetween it's shoulder and wing joint. You hurry back into the armory as the dragon roars in outrage. The dragon roars again. Then, to your suprise, the dragon begins speaking, 'To the brave little squirt that just stabbed me, I would be much obliged if you would come and face me. No one can go injure me like that and get away with it.'")
        typingInput(" 'Don't you agree?' (answer the question): ")
        typingPrint(f'''The dragon laughs, 'Funny. Little human what is your name?' '{name},' you respond.''')
        typingPrint("'Ha!' cackles the dragon. 'Stupid name.' The dragon charges you. ")
        dragon_charge = typingInput('''You...
        1) run
        2) grab another spear
        3) grab your extra William Shakespeare script
        - ''')
        if dragon_charge == '1':
            typingPrint('''You turn and run. The dragon quickly overtakes you and the last thing that you see is the back of it's throat.
    GAME OVER\n''')
        elif dragon_charge == '2':
            typingPrint('''You leap for the armory for another spear. The dragon catches you before you make it. The dragon carries you into the sky where it throws you unto the air and eats you.
    GAME OVER\n''')
        elif dragon_charge == '3':
            typingPrint("You have to do some quick thinking. You decide to pull out your pocket Shakespeare book. It hold every script to every one of his plays and sonnets. You begin to swiftly read, Sonnet 18: Shall I Compare Thee to a Summer's Day? The dragon stops; it is confused. As you finish the sonnet, the dragon begins to be flattered. You dive into Sonnet 138 and by the end the dragon is very flattered. 'I will tell you what,' the dragon muses, 'I will spare you if you will journey with me and tell me one of these every day.'")
            dragon_compromise = typingInput('''Do you agree?
            1) yes
            2) no
            - ''')
            if dragon_compromise == '2':
                typingPrint('''You say no. The dragon ripps you apart and eats you like a spaghetti noodle.
        GAME OVER\n''')
            elif dragon_compromise == '1':
                typingPrint("The dragon is pleased when you say yes. It picks you up and flies away.")
                time.sleep(3)
                Chaptertwo()
            else:
                typingPrint("Syntax Error 01: Invalid Input")
                return Chapterone()
        else:
            typingPrint("Syntax Error 01: Invalid Input")
            return Chapterone()
    else:
        typingPrint("Syntax Error 01: Invalid Input")
        return Chapterone()
def Chaptertwo():
    clearScreen()
    typingPrint("CHAPTER TWO")
    print('')
    typingPrint('''The dragon takes you to its lair. It tells you that it never was named.''')
    global dragon_name
    dragon_name = typingInput("What do you want to name the dragon?")
    typingPrint(f'''You name it {dragon_name}. {dragon_name} then tells you she is female. Days pass as you explore the lair and tell Shakespearean poetry to {dragon_name}. You have enough food, even if it is raw... or blackened to a crisp. Most of the time the food that she brings is cow. One day as you are exploring the cave, you come to a place where you have not been before.''')
    arches = typingInput('''There are three stone arches. Which one do you take?
        1) The arch on the right
        2) The arch on the left
        3) The arch in the middle.
        - ''')
    if arches == '1':
        typingPrint('''You walk into the arch on the right and stroll for a little while. It is a dead end. You walk back to the entrance. Surprisingly, it is also a dead end. You end up starving to death.
GAME OVER\n''')
    elif arches == '2':
        typingPrint('''You head down the left archway. You walk for about nine minutes, fifteen seconds, and thirty-six miliseconds before you enter a large cave. It has intricate carvings all over the walls. You explore it very much, looking everywhere, taking everything in. About two hours, forty-one minutes, twenty-three seconds, and fifty-eight miliseconds pass. You run into a wall. As you rub your head you notice small holes in the wall. You inspect them closer...and a worm flies out. It slaps against your skin and sticks there. More worms fly out of the wall and you suffer death by worms.
GAME OVER\n''')
    elif arches == '3':
        typingPrint('''You choose the middle arch. As you walk through it a cool breeze blows your hair back, causing your toupee to fall off. As you hurredly pick it back up and put it on you notice a faint scent wafting down the hall. It smells gross and sweet at the same time. You follow the scent down the hall where you come to a large cave. In this cave there is what seems to be a large nest. It is shaped like a large ant nest. You explore some more, letting your eyes take in everything about this cave. As you peek around in it you come to a wall with small holes in it. You look through the holes. You can barely make out another cave with intricate carvings all over the walls. As you are looking through the holes something slaps against your back. You grab at your back and pull the slimy thing off. It is a large worm. As you look at it it opens a large mouth full of tiny teeth. A yelp and drop the worm. The worm, frightened, lashes out and bites you. Your arm begins to burn with pain as the worm injects its poison. You grab the worm and yank it off of you. In your angry pain you hold fast to both ends of the worm and rip it in half. The worm pops and blood, guts, and slime fly ten feet in every direction. The ant-like nest begins buzzing. Multiple worms fly out, enraged at the scent of a worms blood. They fly towards you, a hissing mass of slime. You run as fast as you can, adrenaline pumping through your veins energizing you and causing your heart to beat very fast. The worms follow you, their mouths open wide in a loud scream. You grab a sharp flat rock and throw it into the worms like a frisbee. Blood, guts, and slime explode everywhere splattering the rocks that you stand on. This makes the worms even more enraged. You find the entrance that you came from and run back to the main cavern. ''')
        worms_in_cavern = typingInput(f'''Do you...
            1) hide
            2) run
            3) yell for {dragon_name}
            - ''')
        if worms_in_cavern == '1':
            typingPrint(''' You quickly hide underneath piles of treasure, but the worms smell you and you suffer death by worms.
    GAME OVER\n''')
        elif worms_in_cavern == '2':
            typingPrint('''You run even faster out of the cave entrance. Surprisingly, the worms don't follow you. It appears as if the worms don't like sunlight. You keep running anyway to get as much space in between you and the worms. However, you don't look where you're running and you run off a cliff.
    GAME OVER\n''')
        elif worms_in_cavern == '3':
            typingPrint(f'''You arrive in the main cavern and scream for {dragon_name}'s help. {dragon_name}, who was sleeping wakes up and looks at the situation. At the sight of the worms, {dragon_name} seems enraged. She leaps into the air and roars. The roar jars your head. As you recover and look back at the worms you realize that the roar had a similar, more powerful effect on them. The worms are now not in a group, but on the floor writhing in agony. {dragon_name} dives towards them and slashes them apart with her claws, blood flying everywhere. As she tears the worms to shreds, other worms come up into the cave seemingly from nowhere. They surround {dragon_name} and bite. {dragon_name} roars again. All the unattached worms fall to the ground, stunned.''')
            attack_worms = typingInput(''' You quickly...
                1) die
                2) grab a sword and attack the stunned worms
                3) run
                - ''')
            if attack_worms == '1':
                typingPrint('''You die.
        GAME OVER\n''')
            elif attack_worms == '3':
                typingPrint('''You run out of the cave entrance. Surprisingly, the worms don't follow you. It appears as if the worms don't like sunlight. You keep running anyway to get as much space in between you and the worms. However, you don't look where you're running and you run off a cliff.
        GAME OVER\n''')
            elif attack_worms == '2':
                typingPrint(f'''You grab a sword from the pile of treasure that {dragon_name} has collected from various places. The sword is heavy and dull but it'll do. You charge around the room slashing at the stunned worms and occasionally killing a worm attached to {dragon_name}.The worms begin to recover and they attack you. You swing the dull sword in their midst, ripping several apart. A couple of them grab onto you, injecting their poison. You pop them with your fingers. {dragon_name} roars again, bringing to your attention that she needs help. More worms are all over her body, covering her legs, wings, tail, and neck. You run to {dragon_name}, your path cleared by the dragons roar. The ground is slippery from worm innards. As you near {dragon_name} you slip and fall. You bang your head and pass out.''')
                time.sleep(3)
                Chapterthree()
            else:
                typingPrint("Syntax Error 01: Invalid Input")
                return Chaptertwo()
        else:
            typingPrint("Syntax Error 01: Invalid Input")
            return Chaptertwo()
    else:
        typingPrint("Syntax Error 01: Invalid Input")
        return Chaptertwo()


def Chapterthree():
    clearScreen()
    typingPrint("CHAPTER THREE")
    print('')
    time.sleep(1.5)
    typingPrint(f'''You wake up underneath a pile of gold coins. It is very warm and heat is radiating from your left side. You push to the top of the pile. To your horror there is a burning pile of worms next to you. {dragon_name} is laying down next to the fire, nursing her wounds. You sit up, rubbing your head. You are covered head to toe in worm guts. You are glad that you missed most of the fight. As you clean yourself up you notice that there are noticably more worms in the room than when you were awake. Worms are stuck to the wall, ceiling, and floors. Everywhere you look there are worms. {dragon_name} stirs, shifting the enormous pile of gold and silver. She groans as the movement reopens the worm wounds. {dragon_name}'s cuts and bruises are much worse than your own. You only have about five or six worm wounds; {dragon_name} has twenty to thirty of them. Thankfully the poison from the worms isn't very powerful and doesn't cause permanent damage; the poison only causes pain. However this can cause you heart to overwork itself, leading to heart failure. You try to calm down, taking deep breaths and counting. As you recover, {dragon_name} lifts her head. She growls. "The master worm is coming. Hide." {dragon_name} says. You dive under the pile of gold again. Seconds later you hear a loud screaming, louder than the screaming of all of the worms in the nest. It must be the master worm. The floor starts shaking and the gold begins shifting off of you. You burrow deeper into the coins. A large sound like an explosion vibrates from above you. The master worm is in the cavern.''')
    master_worm = typingInput('''Do you...
    1) run
    2) stay hidden
    3) surprise attack!
    - ''')
    if master_worm == '1':
        typingPrint('''You burst from your hiding place and run to the exit. You slip on worms guts and hit your head on a sharp rock. Skill issue.
GAME OVER''')
    elif master_worm == '2':
        typingPrint(f'''You stay hidden. The fight for dominance starts with fire and screams and roars. Then {dragon_name} steps on you.
GAME OVER''')
    elif master_worm == '3':
        typingPrint(f'''You stay hidden. The fight for dominance starts with fire and screams and roars. You remember the many wounds on {dragon_name} and the sword that you used to kill the other worms. It has to be near you... you search around yourself with your hands as quietly as possible. Your hand grasps the handle of a sword. You quietly climb out of the pile of glittery goods the sound masked by the duel going on on the other side of the cavern. You pull yourself free and notice that the sword that you're holding is a different sword. It is very sharp and gleaming. It has gold and silver decorations. You charge the master worm. It is distracted by {dragon_name}, giving you an opportunity to get close. When you get near the worm, it gets trapped in a headlock by {dragon_name}. It begins thrashing and swinging itself against {dragon_name}. The Master Worm curls it body around {dragon_name} and tries to suffocate it. {dragon_name} bites down on the worms head even harder. The worm is desperate. I raises it's tail and points it down at the back of {dragon_name}'s skull. Slowly, a stinger emerges from the tip of it. With lightning speed the worms tail descends upon the back of {dragon_name}'s skull, injecting a poison far more potent and deadly than the other poisons. {dragon_name} releases the Master Worm and stumbles backward. {dragon_name} is struggling to stand. She falls over, unconscious. You stand dumbfounded.''')
        surprise_attack = typingInput(''' Do you...
        1) Stab at the Master Worm's head
        2) Attack the Master Worm's eyes
        3) Slash at the Master Worm's underbelly
        - ''')
        if surprise_attack == '1':
            typingPrint('''You hold the sword with both hands. You leap up at the Master Worm's head, confident that you can clear the jump. However, the Master Worm moves it's head higher and you fall directly into its mouth.
    GAME OVER''')
        elif surprise_attack == '2':
            typingPrint('''You charge at the Master Worm, your sword held high, the edge flashing in the sunlight trickling in through the entrance of the cavern. As you get close to the Master Worm you level your sword at it's eyes. Your plan is to dodge around the Master Worm's head and blind it with your sword. Your plan works... until it doesn't. You are devoured by the worm.
    GAME OVER''')
        elif surprise_attack == '3':
            typingPrint(f'''You stand still facing the Master Worm. It slides towards you. You stand still. It's right in front of you. You make a quick movement. You dive underneath the pile of gold. The worm follows, burrowing inot the gold behind you. You change directory just in time, moving horizantally. You emerge from the side of the pile. Running up to the exposes underbelly of the worm, you stab it. The blade cuts into the belly easily, but gets stuck. The stab wound on the worm begins swelling at an alarming rate. You yank of the sword as hard as you can. Unfortunately, it is stuck. The swelling becomes too much and bursts, covering you in more warm worm guts. The worm screams and flings it head out of the treasure. You stab it again. This time you're able to pull it out. The wound swells and bursts like the other one. The worm begins swinging around in a rage. You step back holding the sword out. The Master Worm's head swings directly into your sword. You are knocked off your feet and let go of the sword. The worm is screaming louder than ever and the cavern is cavern is shaking from the force of it slamming into the walls, ceiling, and floor. The fortune on the floor is shifting so you cannot get a stable footing. The Master Worm's head has a large, quickly swelling lump on it head. The blister begins to get larger and larger, far more large than the blisters that were on its body. That is because the skin on its head is thicker and more flexible than the skin on its body. Pressure began to build up underneath the Master Worm's skin. The pressure would soon force its way out or crush the worm's brain. If the pressure escapes the worm will live. There's nothing you can do about it though. The skin splits and blood flows out. The worm is angry, but it is dazed. It can no longer see well. The Master Worm writhes and slides out of the cavern. Once in the sunlight, the Master Worm freezes. It slowly turns from pale white to a sunburnt red. Blisters formed and moved about on the worm's skin. Then the blisters began popping. Soon, the Master Worm is missing it's skin and is shivering. You take the sword and finish off the worm. The Master Worm is dead. {dragon_name} is now dead. You have your freedom. And so you begin your trek back to the city that you came from.\n''')
            print('')
            typingPrint('''GAME COMPLETE''')

# put everything for the story above this line. ___________________


if password == "Harold":
    chapter_selection = typingInput("Which chapter would you like  go to (number format)?\n")
    if chapter_selection == '1':
        name = typingInput('''What is your name?
''')
        typingPrint("Welcome to Terronis, %s." % (name))
        time.sleep(3)
        typingPrint(
            ''' Make sure to answer all questions using the answer number, unless it is a typed response''')
        time.sleep(3)
        clearScreen()
        Chapterone()
    elif chapter_selection == '2':
        name = typingInput('''What is your name?
''')
        typingPrint("Welcome to Terronis, %s." % (name))
        time.sleep(3)
        typingPrint(
            ''' Make sure to answer all questions using the answer number, unless it is a typed response''')
        time.sleep(3)
        clearScreen()
        Chaptertwo()
    elif chapter_selection == '3':
        name = typingInput('''What is your name?
''')
        typingPrint('Welcome to Terronis, %s.' % (name))
        time.sleep(3)
        typingPrint(
            ''' Make sure to answer all questions using the answer number, unless it is a typed response.\n''')
        time.sleep(3)
        global dragon_name
        dragon_name = typingInput("What do you want to name the dragon?\n")
        clearScreen()
        Chapterthree()
    else:
        typingPrint("Syntax Error 01: Invalid Input")
else:
    credits()
    Chapterone()

# Credits take ~31 seconds to complete
