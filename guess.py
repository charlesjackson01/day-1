import random

secret = random.randint(1,10)

guess = 0 
while guess != secret:
    guess = int(input("Guess (1-10):"))

print("you got it!")
