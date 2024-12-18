import random

def print_man(wrongGuesses):
    for line in hangman_art[wrongGuesses]:
        print(line)

words = ("apple", "banana", "orange", "pineapple")

hangman_art = { 0: ("   ",
                    "   ", 
                    "   "),
                1: (" o ",
                    "   ", 
                    "   "),
                2: (" o ",
                    " | ", 
                    "   "),
                3: (" o ",
                    "/| ", 
                    "   "), 
                4: (" o ",
                    "/|\\", 
                    "   "),
                5: (" o ",
                    "/|\\", 
                    "/  "),
                5: (" o ",
                    "/|\\", 
                    "/ \\ ")}

word = random.choice(words)
currentWord = ["_" for x in range(0, len(word))]
print(currentWord)
wrongGuesses = 0
is_running = True

print("*************************************")
print("Hello! Welcome to Will's Hangman Game")
print("*************************************")

while (is_running):
    letter = input("Enter your letter guess. ")

    is_letter = False

    while not is_letter:
        if letter.isdigit() or len(letter) > 1:
            letter = input("Invalid input. Please enter a letter.")
        else:
            is_letter = True

    if letter.lower() in word:
        for x in range(0, len(word)):
            if letter == word[x]:
                currentWord[x] = letter

        print(currentWord)

    else:
        print("-------------------------------------------")
        print("Wrong guess! Your hangman now looks like...")
        wrongGuesses = wrongGuesses + 1
        print(currentWord)
        print_man(wrongGuesses)

    if wrongGuesses == 6:
        print("You lost :(")
        is_running = True
    elif "_" not in currentWord:
        print("You won! :)")
        is_running = True




    

