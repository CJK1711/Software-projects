#Write a function that will welcome the user to the game Mastermind and explain the rules of the game in a clear and concise manner. The function should be called welcomeMessage()
def welcomeMessage():
    print("Welcome to Mastermind!")
    print("The rules of the game are as follows:")
    print("1. The computer will generate a secret code consisting of 4 colors (repetition is allowed).")
    print("2. You have 10 attempts to guess the code.")
    print("3. After each guess, you will be told how many colors are in the correct position and how many are in the code but in the wrong position.")
    print("4. Try to guess the code in as few attempts as possible!")
    print()

#Write a function called gameSelect() that prints text asking the user if they want to play Mode 1 or Mode 2. Explain that mode 1 is the standard game where the user tries to guess the computer's code, and mode 2 is where the computer tries to guess the user's code
def gameSelect():
    print("Please select a game mode:")
    print("Mode 1: You try to guess the computer's code.")
    print("Mode 2: The computer tries to guess your code.")
    #write a statement to prompt the user for input and validate that the input is either 1 or 2. If the input is invalid, print an error message and prompt the user again until they enter a valid input.
    while True:
        mode = input("Enter 1 for Mode 1 or 2 for Mode 2: ").strip()
        if mode in ['1', '2']:
            return int(mode)
        else:
            validate_game_mode_input_message(mode)

def modeConfirm(mode):
    if mode == 1:
        print("Mode 1 selected. The code has been generated.")
    elif mode == 2:
        print("Mode 2 selected. Please think of a secret code and the computer will try to guess it.")


def guess(guessCount, message="Enter your input (the valid colours are: green, red, yellow, blue, white, black)", valid_options=None):
    """
    Prompts the user with a message and validates input against optional options.
    
    Args:
        guessCount (int): The current guess number to display in the prompt
        message (str): The prompt message to display
        valid_options (list): Optional list of valid responses to accept
        
    Returns:
        str: The validated user input
    """
    # implement this command print(f"Invalid color '{color}'. Valid colors are: {', '.join(valid_colors)}") in the validate_color_code function in Logic.py and replace the while loop in get_valid_color_code with a call to this function to prompt the user for input and validate it against the valid colors list. The function should continue to prompt the user until a valid input is received.
    print(f"Guess #{guessCount}: {message}")
    user_input = input().strip()
    return user_input
    
def quitMessage():
    print("Thanks for playing! Goodbye!")

def winMessage(guesses):
    print(f"Congratulations! You've guessed the code in {guesses} guesses!")

def lossMessage(code):
    print(f"Sorry, you've used all your guesses. The correct code was: {', '.join(code)}")
    
valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
#write a function to print error messages for invalid color codes in the validate_color_code function in Logic.py. The function should be called print_color_code_error and should take the invalid color and the list of valid colors as arguments. It should print a message indicating which color is invalid and what the valid colors are.
def print_color_code_error(invalid_color, valid_colors):
    print(f"Invalid color '{invalid_color}'. Valid colors are: {', '.join(valid_colors)}")

#write a function to print an error message for invalid input length in the validate_color_code function in Logic.py. The function should be called print_color_code_length_error and should take the length of the input as an argument. It should print a message indicating that the input is invalid and what the expected length is.
def print_color_code_length_error(input_length):
    print(f"Invalid code length. Please enter exactly 4 colors (you entered {input_length}).")

#write a function that validates get_game_mode input in Master.py and prints an error message if the input is invalid. The function should be called validate_game_mode_input and should take the user's input as an argument. It should print a message indicating that the input is invalid and what the valid options are.
def validate_game_mode_input_message(user_input):
    
        print("Invalid input. Please enter 1 for Mode 1 or 2 for Mode 2.")

#write a function called gameResults() that prints out if the user won or lost the game. if the user won, print (you won in i amount of guesses) and if the user lost, print (you lost. The correct code was: code) 
def gameResults(won, guesses, code): 
    if won: 
        print(f"You won in {guesses} guesses!") 
    else: 
        print(f"You lost. The correct code was: {code}") 

#write a function guessFeedback() that prints the touple returned by the compareGuesses() function in Logic.py in a user-friendly format. The function should take the feedback touple as an argument and print the number of colors in the correct position and the number of colors in the code but in the wrong position.
def guessFeedback(correct_position, wrong_position):
    print(f"Colors in the correct position: {correct_position}")
    print(f"Colors in the code but in the wrong position: {wrong_position}")

#write a function called resetGame() that asks if the player wants to play again after a game has ended. If the player inputs "yes", the function should call the main() function to start a new game. If the player inputs "no", the function should print a goodbye message and exit the program. The function should continue to prompt the user until they enter a valid response ("yes" or "no"). 
def resetGame():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response == 'yes':
            return response
        elif response == 'no':
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

#write a function called codeCreate() that prompts the user to enter a secret code for Mode 2. The function should validate the input using the validate_color_code function from Logic.py and return the valid code as a list of colors. The user should enter the colors separated by commas
def codeCreate():
    from Logic import validate_color_code
    while True:
        user_input = input("Enter your code (4 colors separated by commas - the valid colours are green, red, yellow, blue, white, black):\n").strip()
        if user_input.lower() in ['quit', 'q']:
            return "quit"
        if validate_color_code(user_input, valid_colors):
            return [color.strip().lower() for color in user_input.split(',')]
        
#write a function called botGuessOut that takes the bot's guess and the guess count as arguments and prints the bot's guess in a user-friendly format. The function should print the guess count and the colors guessed by the bot.
def botGuessOut(guessCount, botGuess):
    print(f"Bot's Guess #{guessCount}: {', '.join(botGuess)}")
        
#write a function called usrFeedback that prompts the user to provide feedback on the computer's guess in Mode 2. The function should ask the user to enter the number of colors in the correct position and the number of colors in the code but in the wrong position. The function should validate that the input is a non-negative integer and return the feedback as a tuple.
def usrFeedback(code):
    while True:
        try:
            print(f"Your code: {', '.join(code)}") 
            correct_raw = input("Enter the number of colors in the correct position (or 'q' to quit): ").strip().lower()
            if correct_raw in ['quit', 'q']:
                return "quit"
            wrong_raw = input("Enter the number of colors in the code but in the wrong position (or 'q' to quit): ").strip().lower()
            if wrong_raw in ['quit', 'q']:
                return "quit"

            correct_position = int(correct_raw)
            wrong_position = int(wrong_raw)
            if correct_position < 0 or wrong_position < 0:
                print("Please enter non-negative integers for feedback.")
                continue
            if correct_position + wrong_position > 4:
                print("The total of correct and wrong position feedback cannot exceed 4. Please enter valid feedback.")
                continue
            return (correct_position, wrong_position)

        except ValueError:
            print("Invalid input. Please enter non-negative integers for feedback.")

def cheaterMessage(guess):
    print("Nice try cheater, but your feedback doesn't match the expected feedback based on your secret code and the computer's guess. Please provide accurate feedback.")
    print(f"Bot's Guess: {', '.join(guess)}")

def botWinMessage(guesses):
    print(f"The computer guessed your code in {guesses} guesses! Better luck next time!")

def botLossMessage(code):
    print(f"The computer failed to guess your code. The correct code was: {', '.join(code)}. Congratulations, you win!")