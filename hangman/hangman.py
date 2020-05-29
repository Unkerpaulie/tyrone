import random
import time


# create list of words
words = ["ADVICE", "BREATHE", "COMPLAIN", "DELIVER", "EXAMPLE", "FORGETFUL", "GRADUATE", "HIBERNATE", "INFERIOR", "JUSTIFY"]
# choose a random word from the list
word = random.choice(words)

chances = 5
letters_guessed = []
letter = ""


def clear():
    # prints a number of empty lines to look as if the screen is cleared
    print("\n" * 40)


def display_word(letters):
    # displays dashes for each letter of the word and fills in as letters are guessed
    display = ""
    for i in range(0, len(word)):
        if word[i] in letters:
            display += word[i]
        else:
            display += "-"
    return display


# welcome user
print("Hello, Welcome to Hangman")
input("Press enter to begin...")
# main game loop
while chances > 0:
    clear()
    # only accept 1 letter input, store it as uppercase
    if len(letter) == 1:
        letters_guessed.append(letter.upper())
        if letter.upper() in word:
            print(f"Excellent! {letter.upper()} is in the word.")
        else:
            print(f"Sorry! {letter.upper()} is not in the word.")
            chances -= 1

    print(display_word(letters_guessed))
    print(f"Chances left: {chances}")
    # check if game won or lost
    if chances == 0:
        print(f"Sorry, you lost the game. The word was {word}")
        break
    elif "-" not in display_word(letters_guessed):
        print("Great job! You got the word!")
        break
    else:
        letter = input("Guess a letter: ")

print("Game Over")