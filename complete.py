import random

words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'gorilla', 'house', 'ice', 'jacket', 'kangaroo', 'lion', 'monkey', 'nose', 'orange', 'pizza', 'queen', 'rain', 'sun', 'tree', 'umbrella', 'violin', 'water', 'xylophone', 'yacht', 'zebra']
   
def get_word():
    """Prompt the user for a word and return it."""
    letter = input("Enter a letter: ").lower().strip()
    while not letter.isalpha():
        print("Invalid input. Please enter a letter.")
        letter = input("Enter a letter: ").lower().strip()
    return letter


def get_yes_no_choice(prompt):
    """Ask the user for a yes/no choice and return True for 'yes' and False for 'no'."""
    while True:
        choice = input(prompt + " (yes/no) ").lower().strip()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")




def get_computer_word(current_word):
    len = current_word.length()
    """Return a random word from a list of words."""
    for word in words:
        if word.startswith(current_word):
            return word

def play_game():
    """Play a game of word chain against the computer."""
    print("Welcome to Word Chain!")
    print("You will take turns with the computer to say a word that begins with the last letter of the previous word.")
    print("If you can't think of a word or if you repeat a word, you lose.")
    print("Let's start!")
    
    current_word = ""
    
    
    while True:
        print("Word: " + current_word)
        # Player's turn
        player_word = get_word()
        current_word += player_word
        
        # Computer's turn
        print("The computer's turn:")
        computer_word = get_computer_word()
        current_word += computer_word[len + 1: len + 2]
        
        print("Word: " + current_word)


        choice = get_yes_no_choice("Do you want to chanllenge?")
        if choice:
            print("You chose to challenge. The word is " + computer_word)

play_game()
