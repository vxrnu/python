import random
def guess_word():
    words = ["apple", "banana", "grape", "cherry", "orange"]
    words = random.choice(words)
    guess = ""
    guesses = 0
    while guess != words:
        print(words[0+1])
        guess = input("Guess a fruit: ")
        if guess == words:
            print("You guessed it")
            guesses += 1
        else:
            print("Try again")
            guesses += 1
    print(f"It took you {guesses} guesses")
guess_word()