import random
import nltk
from nltk.data import find
from nltk.corpus import words

# Check if the 'words' corpus is already downloaded
try:
    find('corpora/words.zip')  # Check if the words corpus exists
except LookupError:
    nltk.download('words')

# ASCII art for hangman stages
hangman_stages = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    ''', 
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    '''
]

# Define the function to choose a word based on difficulty
def choose_word(difficulty):
    word_list = words.words()
    
    if difficulty == "easy":
        word_list = [word for word in word_list if len(word) <= 4]
    elif difficulty == "medium":
        word_list = [word for word in word_list if 5 <= len(word) <= 7]
    elif difficulty == "hard":
        word_list = [word for word in word_list if len(word) >= 8]
    else:
        return None  # Return None if the difficulty is invalid

    return random.choice(word_list)  # Choose a random word from the filtered list

# Function to display the current status of the word with blanks for unguessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Function to play the hangman game
def hangman():
    print("\n★ Hangman ★")
    difficulty = input("\nChoose difficulty (easy/medium/hard): ").lower()
    
    # Check if the difficulty input is valid
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid input! Please choose 'easy', 'medium', or 'hard'.")
        difficulty = input("\nChoose difficulty (easy/medium/hard): ").lower()
    
    word_to_guess = choose_word(difficulty)
    
    guessed_letters = set()
    attempts = 6  # The number of incorrect guesses allowed

    while attempts > 0:
        # Display the current hangman stage based on remaining attempts
        print(hangman_stages[6 - attempts])
        
        # Display the current status of the word
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent status:", current_display)
        
        # Check if the word has been completely guessed
        if "_" not in current_display:
            print("Congratulations! You've won! The word was:", word_to_guess)
            break
        
        # Ask the user to guess a letter or the entire word
        guess = input("Guess a letter or the entire word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():  # Guess is a single letter
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                guessed_letters.add(guess)
                if guess in word_to_guess:
                    print("Good guess!")
                else:
                    attempts -= 1
                    print("Incorrect guess. Attempts left:", attempts)
        
        elif len(guess) == len(word_to_guess) and guess.isalpha():  # Guess is the whole word
            if guess == word_to_guess:
                print("Congratulations! You guessed the word:", word_to_guess)
                break
            else:
                attempts -= 1
                print("Incorrect guess. Attempts left:", attempts)
        
        else:
            print("Invalid input. Please enter a valid letter or the entire word.")
    
    # Check if the user ran out of attempts
    if attempts == 0:
        print(hangman_stages[6])  # Show the final stage of the hangman (full drawing)
        print("\nSorry, you've run out of attempts. The word was:", word_to_guess)

# Call the hangman function to start the game
hangman()