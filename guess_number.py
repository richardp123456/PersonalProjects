import random

def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Too low, guess again")
        elif guess > random_number:
         print("too high, guess again")
    print(f"correct, the right number is {random_number}")
guess(10)