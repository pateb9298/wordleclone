import random
import tkinter as tk
import enum
from tkinter import *
from tkinter import messagebox

def load_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()  # Read each line as a separate word
    return words

# Load the words from 'words.txt'

word_list = load_words('words.txt')

# Choose a random word from the list for the game
import random
# The word to guess
word = random.choice(word_list)
# Initialize the Tkinter root window
root = Tk()

# Define color codes for different states (correct letter, wrong position, etc.)
GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"
GRAY = "#787c7f"

# Set the background color of the window to white
root.config(bg=WHITE)

# Initialize the guess counter
guessnum = 1

# Create an input field for the user to enter their guess
wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

# Function to process the user's guess
def getGuess():

    global word
    guess = wordInput.get() # Get the user's guess from the input field

    global guessnum
    guessnum += 1 # Increment the guess counter

    if guessnum <= 5:  # Allow up to 5 guesses

         # Check if the guess is 5 characters long
        if len(guess) == 5:

            if word == guess: #If the guess is CORRECT
                messagebox.showinfo("Correct!", f"Correct! the word was {word.title()}")
            else:             #If the guess is INCORRECT
                for i, letter in enumerate(guess): # Iterate over each letter in the guess

                    # Create a label for each letter and display it on the grid
                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, padx=10, pady=10)

                    if letter == word[i]: #If the letter is correct and in the correct position
                        label.config(bg=GREEN, fg=BLACK)
                    
                    no_letter = []
                    if letter in word and not letter == word[i]: # If the letter is correct but in the wrong position
                          for j in word:
                            if letter==j:
                                no_letter.append(letter)
                                label.config(bg=YELLOW)
                    
                    if letter not in word: # If the letter is not in the word
                        label.config(bg=GRAY, fg=WHITE)

        else:
            # Show an error message if the guess is not 5 characters long
            messagebox.showerror("Please use 5 characters in your guess")
    
    else:
        # Show an error message if the user has used all their guesses
        messagebox.showerror("You lose!", f"You Lose! The word was {word}")

# Create a button that triggrs the getGuess function when clicked
wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)


# Run the Tkinter event loop

root.mainloop()