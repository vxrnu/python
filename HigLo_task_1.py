import random
def guess_number():
    number = random.randint(1, 20)
    guess = 0
    guesses = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 20:"))
        if guess < number:
            print("Too low")
            guesses += 1
        elif guess > number:
            print("Too high")
            guesses += 1
    print("You guessed it")
    print(f"It took you {guesses} guesses")
guess_number()