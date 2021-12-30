import random
answer = random.randint(1 , 99)

guess = input(" what is your guess? ")
guess = int(guess)

while guess != answer:
    if guess > answer:
        print("my number is smaller!")
    else:
        print("my number is larger!")
    guess = input(" what is your guess? ")
    guess = int(guess)

print("wow you did it!!!!!")