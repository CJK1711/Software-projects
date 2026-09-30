import code
import time
import os
import sys
# Ensure the repo root is on PYTHONPATH so `import src.*` works reliably.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.GameUI import guess, guessFeedback, welcomeMessage, gameSelect, print_color_code_error, modeConfirm, quitMessage, winMessage, lossMessage, resetGame, codeCreate, usrFeedback, botWinMessage, botGuessOut, botLossMessage, cheaterMessage
from src.Logic import validate_color_code, generateCode, compareGuess, cheaterCheck, guessAlgorithm

#Write a function called main that will call the welcomeMessage() function from GameUI.py
def main():
    welcomeMessage()
    mode = gameSelect()
    modeConfirm(mode)
    if mode == 1:
        mode1()
    else:
       mode2()
        
#create a function called mode1 that will call generateCode() function and the creates a loop of 10 iterations, leave it empty for now 
def mode1():
    gameWin = False
    code = generateCode()
    for i in range(10): 
        usrInput = guess(i + 1)
        if usrInput.lower() in ['quit', 'q']:
            quitMessage()
            reset = resetGame()
            if reset == 'yes':
                main()
                return
            elif reset == 'no':
                quitMessage()
                return

        #write a statement to keep prompting the user for input until they enter a valid color code using the validate_color_code function from Logic.py. The valid colors are "green", "red", "yellow", "blue", "white", and "black". The user should enter the colors separated by commas (e.g. "red, green, blue, yellow").
        while not validate_color_code(usrInput, ["green", "red", "yellow", "blue", "white", "black"]):
            #write a statement to check if the user input a quit or q
            if usrInput.lower() in ['quit', 'q']:
                quitMessage()
                reset = resetGame()
                if reset == 'yes':
                    main()
                    return
                elif reset == 'no':
                    quitMessage()
                    return
            usrInput = guess(i + 1)
        exact, partial = compareGuess(usrInput, code)
        guessFeedback(exact, partial)
        if exact == 4:
            winMessage(i + 1)
            gameWin = True
            break
    if not gameWin and usrInput.lower() not in ['quit', 'q']:
        lossMessage(code)
    reset = resetGame()
    if reset == 'yes':
        main()
        return
    elif reset == 'no':
        quitMessage()
        return

#create a function called mode2 that will create a loop of 10 iterations, leave it empty for now 
def mode2():
    gameWin = False
    code = codeCreate()
    if code in ['quit', 'q']: #user chose to quit while creating code
        quitMessage()
        reset = resetGame()
        if reset == 'yes':
            main()
            return
        elif reset == 'no':
            quitMessage()
            return
    prevGuesses = []
    prevFeedback = []
    for i in range(10): 
        time.sleep(2) #shhhh the bot is thinking 
        botGuess = guessAlgorithm(prevGuesses, prevFeedback, i)
        #create a variable called prevGuesses that will store the bot's previous guesses and a variable called botFeedback that will store the user's feedback for each guess. These variables should be updated after each guess and feedback is received.
        botGuessOut(i + 1, botGuess)
        botFeedback = usrFeedback(code)
        if isinstance(botFeedback, str) and botFeedback.lower() in ['quit', 'q']:
            quitMessage()
            reset = resetGame()
            if reset == 'yes':
                main()
                return
            elif reset == 'no':
                quitMessage()
                return
        
        cheating_msg = cheaterCheck(botFeedback, botGuess, code)
        if isinstance(cheating_msg, str):
            expected_feedback = compareGuess(botGuess, code)
            if botFeedback != expected_feedback:
                cheaterMessage(botGuess)
                botFeedback = expected_feedback
        prevGuesses.append(botGuess)
        prevFeedback.append(botFeedback)
        if botFeedback[0] == 4:
            botWinMessage(i + 1)
            gameWin = True
            break
    if not gameWin: #functionally impossible for the bot to lose, but just in case
        botLossMessage(code)
    reset = resetGame()
    if reset == 'yes':
        main()
        return
    elif reset == 'no':
        quitMessage()
        return

if __name__ == "__main__":
    main()