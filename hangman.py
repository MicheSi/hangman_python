import random

name = input("Enter your name: ")
print(name, "- Have fun guessing!")

words = [
    "programming",
    "computer",
    "laptop",
    "javascipt",
    "python",
    "java",
    "internet",
    "github",
    "puppies",
    "cupcakes",
    "lollipop",
    "chocolate"
]

word = random.choice(words)

print("\nGuess the letters of the word")
guesses = ""

turns = 10

while turns > 0:
    wrong = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            wrong += 1

    if wrong == 0:
        print("\nYOU WIN!\n")
        print("\nThe word is: ", word)
        break

    guess = input("\nGuess a letter: ")

    guesses += guess

    if guess not in word:
        turns -= 1

        print("\nWrong letter")
        print("\nYou have", + turns, "more guesses")

        if turns == 0:
            print("\nSorry, you lose!")