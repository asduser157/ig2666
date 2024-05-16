import platform
import os
import random
import time
import sys

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.075)
def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def city():
    clearScreen()
    def Hanbergs_Hanburgers():
        menu_items = {
            1: {"name": "Classic Hanberger Meal", "cost": 10.80},
            2: {"name": "Classic Hanberger", "cost": 3.99},
            3: {"name": "Chicken Sandwich", "cost": 2.99},
            4: {"name": "Hanberger Supreme", "cost": 8.50},
            5: {"name": "Double Hanberger", "cost": 5.59},
            5: {"name": "Cheeseburger", "cost": 4.75},
            6: {"name": "Veggie Berger", "cost": 3.99},
            7: {"name": "Small Fries", "cost": 1.50},
            8: {"name": "Medium Fries", "cost": 2.00},
            9: {"name": "Large Fries", "cost": 2.50},
            10: {"name": "Tater Tots", "cost": 4.99},
            11: {"name": "Onion Rings", "cost": 2.75},
            12: {"name": "Coca Cola", "cost": 1.50},
            13: {"name": "Dr. Pepper", "cost": 1.50},
            14: {"name": "Dr. Thunder", "cost": 1.50},
            15: {"name": "Sprite", "cost": 1.50},
            16: {"name": "Starry", "cost": 1.50},
            17: {"name": "Mug Root Beer", "cost": 1.50},
            18: {"name": "Fanta", "cost": 1.50},
            19: {"name": "Chocolate Milk", "cost": 1.75},
            20: {"name": "Orange Juice", "cost": 1.75},
            21: {"name": "Lemonade", "cost": 3.99},
            22: {"name": "Limeade", "cost": 3.99},
            23: {"name": "Ice Cream", "cost": 3.12},
            24: {"name": "Vanilla Shake", "cost": 4.99},
            25: {"name": "Chocolate Shake", "cost": 4.99},
            26: {"name": "Berry Shake", "cost": 4.99},
            27: {"name": "Water", "cost": 0.99},
            28: {"name": "Hanberg Sauce", "cost": 0.50},
        }

        typingPrint("Welcome to Hanberg's Hanbergers!")
        typingPrint("\nHere's the menu:\n")
        for number, details in menu_items.items():
            print(f"{number})  {details['name']} - Cost: ${details['cost']:.2f}")
        for number, details in menu_items.items():
            print(f"{number})  {details['name']} - Cost: ${details['cost']:.2f}")
        user_input = typingInput("\nEnter the menu item numbers to order. If ordering multiple food items, separate each one of the numbers by a comma and a space, then press 'Enter' once you have finished ordering:\n")
        order_numbers = [int(num) for num in user_input.split(", ") if num.strip().isdigit()]
        orders = [menu_items[number] for number in order_numbers if number in menu_items]
        print("Order received.")
        if orders:
            subtotal = sum(order["cost"] for order in orders)
            total_cost = subtotal + (subtotal*0.105)
            typingPrint("\nReceipt:")
            typingPrint("\n------------------------------\n")
            for order in orders:
                typingPrint(f"{order['name']}: ${order['cost']:.2f}\n")
            typingPrint("------------------------------\n")
            typingPrint(f"Subtotal: ${subtotal:.2f}\n")
            typingPrint(f"Tax: ${(subtotal*0.105):.2f}\n")
            typingPrint(f"Total Cost: ${total_cost:.2f}\n")
        else:
            print("Syntax Error 01: Invalid Input")
        repeat = input("\n\nType '0' to start over, or type anything else to exit the program.\n")
        if repeat == '0':
            city()
        else:
            clearScreen()
            sys.exit()

    def IBRR():
        menu_items = {
            1: {"name": "🍔  Deluxe Cheeseburger", "cost": 6.99},
            2: {"name": "🥗  Bacon Ranch Salad", "cost": 5.99},
            3: {"name": "🍲  Creamy Potato and Cheese Soup", "cost": 6.99},
            4: {"name": "🍝  Spaghetti Basil Bowl", "cost": 7.99},
            5: {"name": "🍗  Barbecued Pork and Drumsticks", "cost": 5.99},
            6: {"name": "🌯  Cheesy Rice and Bean Burrito", "cost": 4.99},
            7: {"name": "🍟  Salted French Fries; Small Box", "cost": 0.99},
            8: {"name": "🍟  Salted French Fries; Regular Box", "cost": 1.99},
            9: {"name": "🍟  Salted French Fries; Jumbo Box", "cost": 2.99},
            10: {"name": "🍤  Shrimp Bites; Small Box", "cost": 0.99},
            11: {"name": "🍤  Shrimp Bites; Regular Box", "cost": 1.99},
            12: {"name": "🍤  Shrimp Bites; Jumbo Box", "cost": 2.99},
            13: {"name": "🧀  Melty Cheese Curds; Small Box", "cost": 0.99},
            14: {"name": "🧀  Melty Cheese Curds; Regular Box", "cost": 1.99},
            15: {"name": "🧀  Melty Cheese Curds; Jumbo Box", "cost": 2.99},
            16: {"name": "🍶  Lightly Iced Water; Small", "cost": 0.09},
            17: {"name": "🍶  Lightly Iced Water; Regular", "cost": 0.19},
            18: {"name": "🍶  Lightly Iced Water; Jumbo", "cost": 0.39},
            19: {"name": "🥤  Mystery Soda; Small", "cost": 0.49},
            20: {"name": "🥤  Mystery Soda; Regular", "cost": 0.69},
            21: {"name": "🥤  Mystery Soda; Jumbo", "cost": 0.99},
        }
        array1 = ["Sprite", " Mug Root Beer", "Mountain Dew", "Coca-Cola", "Pepsi", "Fanta", "Dr. Pepper", "Cherry Coke", "Sunkist"]
        mystery = {'21', '20', '19'}
        drink_rand = random.choice(array1)
        typingPrint("Welcome to Ize-Bob's Roaring Restaurant, where food is food.")
        typingPrint("\nHere's the menu:\n")
        for number, details in menu_items.items():
            print(f"{number})  {details['name']} - Cost: ${details['cost']:.2f}")
        user_input = typingInput("\nEnter the menu item numbers to order. If ordering multiple food items, separate each one of the numbers by a comma and a space, then press 'Enter' once you have finished ordering:\n")
        find_it = [string for string in mystery if string in user_input]
        order_numbers = [int(num) for num in user_input.split(", ") if num.strip().isdigit()]
        orders = [menu_items[number] for number in order_numbers if number in menu_items]
        print("Order received.")
        if orders:
            subtotal = sum(order["cost"] for order in orders)
            total_cost = subtotal + (subtotal*0.105)
            typingPrint("\nReceipt:")
            typingPrint("\n------------------------------\n")
            for order in orders:
                typingPrint(f"{order['name']}: ${order['cost']:.2f}\n")
            typingPrint("------------------------------\n")
            typingPrint(f"Subtotal: ${subtotal:.2f}\n")
            typingPrint(f"Tax: ${(subtotal*0.105):.2f}\n")
            typingPrint(f"Total Cost: ${total_cost:.2f}\n")
            if find_it:
                typingPrint("You drink your mystery soda(s). The soda(s) taste like %s." % (drink_rand))
        else:
            print("Syntax Error 01: Invalid Input")
        repeat = input("\n\nType '0' to start over, or type anything else to exit the program.\n")
        if repeat == '0':
            city()
        else:
            clearScreen()
            sys.exit()
    def GCandies():
        menu_items = {
            1: {"name": "🌑  Moon Rocks", "cost": 2.99},
            2: {"name": "💥  Shock Bits", "cost": 3.99},
            3: {"name": "🫠  Melting Pot Mixers", "cost": 2.49},
            4: {"name": "🪄  Proxy Dust", "cost": 7.99},
            5: {"name": "🔥  Flame Outs", "cost": 5.99},
            6: {"name": "🍭  Sweet Teeth", "cost": 4.49},
            7: {"name": "🪞  Mirror Mints", "cost": 4.99},
            8: {"name": "❄️  Frost Bites", "cost": 1.99},
            9: {"name": "🐯  Creature Crackers", "cost": 5.49},
            10: {"name": "🍫  White Fudge", "cost": 6.49},
            11: {"name": "☀️  Sun Stones", "cost": 2.99},
            12: {"name": "🐈  Whisker Cakes", "cost": 1.99},
            13: {"name": "🥤  Dizzy Fizzer", "cost": 1.99},
            14: {"name": "🧼  Clean Slate", "cost": 6.99},
            15: {"name": "🫧  Peak Performance Bubble Gum", "cost": 1.99},
            16: {"name": "💪  Ironhides", "cost": 7.99},
            17: {"name": "🦁  Bestial Biscuits", "cost": 5.49},
            18: {"name": "🦎  Camouflage Caramels", "cost": 3.49},
            19: {"name": "🕷️  Spider Bites", "cost": 2.99},
            20: {"name": "💛  Jawbreakers", "cost": 7.49},
            21: {"name": "🧠  Brain Feed", "cost": 0.99},
        }

        typingPrint("Welcome to Grandy's Candies: The Mystical Sweet Shoppe!")
        typingPrint("\nHere's the menu:\n")
        for number, details in menu_items.items():
            print(f"{number})  {details['name']} - Cost: ${details['cost']:.2f}")
        user_input = typingInput("\nEnter the menu item numbers to order. If ordering multiple food items, separate each one of the numbers by a comma and a space, then press 'Enter' once you have finished ordering:\n")
        order_numbers = [int(num) for num in user_input.split(", ") if num.strip().isdigit()]
        orders = [menu_items[number] for number in order_numbers if number in menu_items]
        print("Order received.")
        if orders:
            subtotal = sum(order["cost"] for order in orders)
            total_cost = subtotal + (subtotal*0.105)
            typingPrint("\nReceipt:")
            typingPrint("\n------------------------------\n")
            for order in orders:
                typingPrint(f"{order['name']}: ${order['cost']:.2f}\n")
            typingPrint("------------------------------\n")
            typingPrint(f"Subtotal: ${subtotal:.2f}\n")
            typingPrint(f"Tax: ${(subtotal*0.105):.2f}\n")
            typingPrint(f"Total Cost: ${total_cost:.2f}\n")
        else:
            print("Syntax Error 01: Invalid Input")
        repeat = input("\n\nType '0' to start over, or type anything else to exit the program.\n")
        if repeat == '0':
            city()
        else:
            clearScreen()
            sys.exit()
    #####

    def Heavenly_Mountain_Creamery():
        menu_items = {
            1: {"name": "Small Vanilla Cone", "cost": 3.79},
            2: {"name": "Medium Vanilla Cone", "cost": 4.79},
            3: {"name": "Large Vanilla Cone", "cost": 5.79},
            4: {"name": "Small Chocolate Cone", "cost": 3.79},
            5: {"name": "Medium Chocolate Cone", "cost": 4.79},
            6: {"name": "Large Chocolate Cone", "cost": 5.79},
            7: {"name": "Small Strawberry Cone", "cost": 3.79},
            8: {"name": "Medium Strawberry Cone", "cost": 4.79},
            9: {"name": "Large Strawberry Cone", "cost": 5.79},
            10: {"name": "Small Special Cone", "cost": 3.79},
            11: {"name": "Medium Special Cone", "cost": 4.79},
            12: {"name": "Large Special Cone", "cost": 5.79},
        }

        typingPrint("Welcome to Heavenly Mountain Creamery! Indulge in the scrumptious dairy goodness of milk from real holy cows.")
        typingPrint("\nHere's the menu:\n")
        for number, details in menu_items.items():
            print(f"{number})  {details['name']} - Cost: ${details['cost']:.2f}")
        user_input = typingInput("\nEnter the menu item numbers to order. If ordering multiple food items, separate each one of the numbers by a comma and a space, then press 'Enter' once you have finished ordering:\n")
        order_numbers = [int(num) for num in user_input.split(", ") if num.strip().isdigit()]
        orders = [menu_items[number] for number in order_numbers if number in menu_items]
        print("Order received.")
        if orders:
            subtotal = sum(order["cost"] for order in orders)
            total_cost = subtotal + (subtotal*0.105)
            typingPrint("\nReceipt:")
            typingPrint("\n------------------------------\n")
            for order in orders:
                typingPrint(f"{order['name']}: ${order['cost']:.2f}\n")
            typingPrint("------------------------------\n")
            typingPrint(f"Subtotal: ${subtotal:.2f}\n")
            typingPrint(f"Tax: ${(subtotal*0.105):.2f}\n")
            typingPrint(f"Total Cost: ${total_cost:.2f}\n")
        else:
            print("Syntax Error 01: Invalid Input")
        repeat = input("\n\nType '0' to start over, or type anything else to exit the program.\n")
        if repeat == '0':
            city()
        else:
            clearScreen()
            sys.exit()


    which_restaurant = input('''Which restaurant do you want to go to?
    1) Hanberg's Hanburgers
    2) Ize Bob's Roaring Restaurant
    3) Grandy's Candies
    4) Heavenly Mountain Creamery
    - ''')
    if which_restaurant == '1':
        clearScreen()
        Hanbergs_Hanburgers()
    elif which_restaurant == '2':
        clearScreen()
        IBRR()
    elif which_restaurant == '3':
        clearScreen()
        GCandies()
    elif which_restaurant == '4':
        clearScreen()
        Heavenly_Mountain_Creamery()
    else:
        print("Syntax Error 01: Invalid Input")
city()
