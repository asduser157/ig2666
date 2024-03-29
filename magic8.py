import random
question = input("Ask the Magic 8 Ball a Yes-or-No Question:\n")
response = ['Yes, definitely', 'It is certain.', 'Affirmative.', 'Reply hazy, try again.', 'Time will tell.', 'Better not tell you now.', 'My sources say no.', 'Negative.', 'Nope, not at all.']
num = random.randint(1,9)
answer = random.choice(response)
print(answer)

