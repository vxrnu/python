word = ["apple", "bones", "chirp", "adieu"]
guesses = 0
green = 0 
orange = 0 
grey = 0 
def mini_wordle():

    # ask for valid input
    while (guesses) < 5:
        guess = str(input("Guess a 5 letter word: ")).lower()
        if len(guess) != 5:
            print("The word must be 5 letters long")
            break


    # score guess against word
    for word in range(len(guess)):
        if word == guess:
            print("You won!")
        elif 

        
            
            
        

# main

# pick a random word from dict

# loop until user wins or surrenders

            mini_wordle(word)