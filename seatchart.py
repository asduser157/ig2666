import random
import time
seat = ["Lauren", "Mason", "Greer", "Covey", "Simon", "Hayden", "Grant", "Dashell", "Lea", "Isaac", "Sariah", "Vicko", "Anna", "Ariah", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]

def please():
    for i in range(27):
        for item in num:
            s = random.choice(seat)
            time.sleep(0)
            print("%s: %s\n" % (item, s))
            seat.remove(s)
        if item == "28":
            break
    if s == "Mason":
        for int in range(6):
            int = int - 1
        if int > 0:
            print("\n" * 30)
            please()
    if s == "Simon":
        for int in range(6):
            int = int - 1
        if int > 0:
            print("\n" * 30)
            please()
    if s == "Hayden":
        for int in range(6):
            int = int - 1
        if int > 0:
            print("\n" * 30)
            please()
    if s == "Vicko":
        for int in range(6):
            int = int - 1
        if int > 0:
            print("\n" * 30)
            please()



please()

