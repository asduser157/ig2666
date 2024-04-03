import random
import time
seat = ["Lauren", "Mason", "Greer", "Covey", "Simon", "Hayden", "Grant", "Dashell", "Lea", "Isaac", "Sariah", "Vicko", "Anna", "Ariah", "", "", "", "", "", "", "", "", "", "", "", ""]
num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]

for i in range(26):
    s = random.choice(seat)
    n = random.choice(num)
    time.sleep(0.6)
    print("%s: %s\n" % (n, s))
    seat.remove(s)
    num.remove(n)

