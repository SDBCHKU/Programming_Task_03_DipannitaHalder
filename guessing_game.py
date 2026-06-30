import random

secret = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == secret:
        print("Correct! Attempts:", attempts)
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")