import random
question = input("Ask the Magic 8 Ball a Yes-or-No Question:\n")
response = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
num = random.randint(1,9)
answer = random.choice(response)
print(answer)

