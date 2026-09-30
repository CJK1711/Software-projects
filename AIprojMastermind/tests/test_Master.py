import os
import sys
from unittest import result

# Ensure the repo root is on PYTHONPATH so `import src.*` works reliably.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import src.Logic as Logic

from src.Logic import validate_color_code, compareGuess, guessAlgorithm, cheaterCheck, generateCode
 
"""Edge case tests """

#


#write a edge case test for the validate_color_code function in Logic.py that tests the input of 5 colours instead of 4
def test_validate_color_code_edge_case():
    # Test input with 5 colors instead of 4
    input_code = "red, green, blue, yellow, white"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is False due to invalid input length
    assert result == False, "Expected False for input with 5 colors instead of 4"


# Boundary/invalid-input test: special characters should be rejected.
def test_validate_color_code_special_characters():
    input_code = "red, green, @@@, blue"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    result = validate_color_code(input_code, valid_colors)

    assert result == False, "Expected False when input contains special characters"

#write a edge case test for the validate_color_code function in Logic.py that tests the input of 3 colours instead of 4
def test_validate_color_code_edge_case_short_input():
    # Test input with 3 colors instead of 4
    input_code = "red, green, blue"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is False due to invalid input length
    assert result == False, "Expected False for input with 3 colors instead of 4"

    #write a edge case test for the validate_color_code function in Logic.py that tests the input of 4 colours but one of them is invalid
def test_validate_color_code_edge_case_invalid_color():
    # Test input with 4 colors but one is invalid
    input_code = "red, green, blue, purple"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is False due to invalid color
    assert result == False, "Expected False for input with an invalid color"

    #write a edge case test for the validate_color_code function in Logic.py that tests the input of 4 colours but all of them are invalid
def test_validate_color_code_edge_case_all_invalid_colors():    
    # Test input with 4 colors but all are invalid
    input_code = "purple, orange, pink, cyan"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is False due to all colors being invalid
    assert result == False, "Expected False for input with all invalid colors"

#write a edge case test for the validate_color_code function in Logic.py that tests the input of 4 colours but they are all valid
def test_validate_color_code_edge_case_all_valid_colors():    
    # Test input with 4 colors and all are valid
    input_code = "red, green, blue, yellow"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is True due to all colors being valid
    assert result == True, "Expected True for input with all valid colors"

#write a edge case test for the validate_color_code function in Logic.py that tests the input of 4 colours but they are all valid and in uppercase
def test_validate_color_code_edge_case_all_valid_colors_uppercase():    
    # Test input with 4 colors and all are valid but in uppercase
    input_code = "RED, GREEN, BLUE, YELLOW"
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Call the function and capture the output
    result = validate_color_code(input_code, valid_colors)
    
    # Assert that the result is True due to all colors being valid even in uppercase
    assert result == True, "Expected True for input with all valid colors in uppercase"

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that is completely correct (e.g. "red, green, blue, yellow" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_all_correct():
    user_guess = "red, green, blue, yellow"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess"

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that has no correct colors (e.g. "purple, orange, pink, cyan" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_no_correct_colors():
    user_guess = "purple, orange, pink, cyan"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 0 and partial == 0, "Expected 0 exact matches and 0 partial matches for a guess with no correct colors"

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that has some correct colors but all in the wrong position (e.g. "green, red, yellow, blue" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_all_correct_colors_wrong_position():
    user_guess = "green, red, yellow, blue"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 0 and partial == 4, "Expected 0 exact matches and 4 partial matches for a guess with all correct colors but in the wrong position"


"""generateCode tests"""


def test_generate_code_happy_path_returns_4_valid_colors():
    code = generateCode()

    assert isinstance(code, list), "Expected generateCode() to return a list"
    assert len(code) == 4, "Expected generateCode() to return exactly 4 colors"
    assert all(color in ["green", "red", "yellow", "blue", "white", "black"] for color in code), (
        "Expected all generated colors to be in the valid color set"
    )


def test_generate_code_boundary_includes_first_and_last_valid_colors(monkeypatch):
    # Boundary-style: force generation to hit the 'ends' of the allowed set.
    forced = iter(["green", "black", "green", "black"])
    monkeypatch.setattr(Logic.random, "choice", lambda _: next(forced))

    code = generateCode()

    assert code == ["green", "black", "green", "black"]


def test_generate_code_edge_case_all_same_color_allowed(monkeypatch):
    # Edge-case: duplicates are allowed; force all picks to be the same.
    monkeypatch.setattr(Logic.random, "choice", lambda _: "red")

    code = generateCode()

    assert code == ["red", "red", "red", "red"]

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that has some correct colors in the correct position and some correct colors in the wrong position (e.g. "red, green, yellow, blue" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_mixed_correct_and_wrong_position():
    user_guess = "red, green, yellow, blue"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 2 and partial == 2, "Expected 2 exact matches and 2 partial matches for a guess with some correct colors in the correct position and some in the wrong position"

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that has some correct colors in the correct position and some incorrect colors (e.g. "red, green, purple, orange" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_mixed_correct_and_incorrect_colors():
    user_guess = "red, green, purple, orange"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 2 and partial == 0, "Expected 2 exact matches and 0 partial matches for a guess with some correct colors in the correct position and some incorrect colors"

#write a edge case test for compareGuess function in Logic.py that tests the input of a user guess that has some correct colors in the wrong position and some incorrect colors (e.g. "green, red, purple, orange" compared to "red, green, blue, yellow")
def test_compare_guess_edge_case_mixed_wrong_position_and_incorrect_colors():
    user_guess = "green, red, purple, orange"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 0 and partial == 2, "Expected 0 exact matches and 2 partial matches for a guess with some correct colors in the wrong position and some incorrect colors"

#write a edge case test for guessAlgorithm function in Logic.py that tests the input of an empty list of previous guesses and feedback (i.e. the bot's first guess)

def test_guess_algorithm_edge_case_first_guess_empty_history():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    first_guess = guessAlgorithm([], [], 0)

    # Should return a 4-color guess
    assert isinstance(first_guess, list) and len(first_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in first_guess)

    # First guess should be two colors repeated twice (e.g. [a, a, b, b])
    assert len(set(first_guess)) == 2
    for color in set(first_guess):
        assert first_guess.count(color) == 2


#write a edge case test for guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback (i.e. the bot's second guess or later)
def test_guess_algorithm_edge_case_subsequent_guess_with_history():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "red", "green", "green"],
        ["yellow", "yellow", "blue", "blue"]
    ]
    feedback = [
        (1, 1),  # 1 correct position, 1 correct color wrong position
        (0, 2)   # 0 correct position, 2 correct colors wrong position
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 2)

    # Should return a 4-color guess
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)

#write a edge case test for guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback where the feedback indicates that the bot has already guessed the correct code (e.g. feedback of (4, 0) for a previous guess)
def test_guess_algorithm_edge_case_correct_code_already_guessed():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "green", "blue", "yellow"]
    ]
    feedback = [
        (4, 0)  # 4 correct positions, 0 correct colors wrong position (code already guessed)
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 1)

    # Should return a 4-color guess (the algorithm should still return a guess even if the code was already guessed)
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)


#write a edge case test for cheaterCheck function in Logic.py that tests the input of feedback that is impossible given the bot's guess and the code (e.g. feedback of (4, 0) for a guess that does not match the code)
def test_cheater_check_edge_case_impossible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "white"]

    feedback = (4, 0)
    result = cheaterCheck(feedback, bot_guess, code)
    assert isinstance(result, str) and "cheating" in result.lower()

#write a edge case test for cheaterCheck function in Logic.py that tests the input of feedback that is possible given the bot's guess and the code (e.g. feedback of (2, 1) for a guess that has 2 colors in the correct position and 1 color in the wrong position)
def test_cheater_check_edge_case_possible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    # This secret produces expected feedback (2 exact, 1 partial) for the guess above.
    code = ["red", "green", "yellow", "white"]

    feedback = (2, 1)
    assert compareGuess(bot_guess, code) == feedback

    result = cheaterCheck(feedback, bot_guess, code)
    assert result is None


#write a edge case test for cheaterCheck function in Logic.py that tests the input of feedback that is on the boundary of being possible (e.g. feedback of (3, 1) for a guess that has 3 colors in the correct position and 1 color in the wrong position, which is possible but very unlikely)
def test_cheater_check_edge_case_boundary_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "yellow"]

    # (3, 1) is not consistent with this guess+code, so it should trigger cheating path
    feedback = (3, 1)
    result = cheaterCheck(feedback, bot_guess, code)
    assert isinstance(result, str) and "cheating" in result.lower()

#write a edge case test for cheaterCheck function in Logic.py that tests the input of feedback that is on the boundary of being impossible (e.g. feedback of (4, 0) for a guess that has 3 colors in the correct position and 1 color in the wrong position, which is impossible)
def test_cheater_check_edge_case_boundary_impossible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "white"]

    feedback = (4, 0)
    result = cheaterCheck(feedback, bot_guess, code)
    assert isinstance(result, str) and "cheating" in result.lower()


"""Boundary tests"""

#write boundry tests for the validate_color_code function in Logic.py that tests the input of 4 valid colors and the input of 4 invalid colors
def test_validate_color_code_boundary_cases():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 valid colors
    input_code = "red, green, blue, yellow"
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of 4 valid colors"

    # Test input of 4 invalid colors
    input_code = "purple, orange, pink, cyan"
    result = validate_color_code(input_code, valid_colors)
    assert result == False, "Expected False for input of 4 invalid colors"

#writ a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where 3 are valid and 1 is invalid
def test_validate_color_code_boundary_case_mixed_colors():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where 3 are valid and 1 is invalid
    input_code = "red, green, blue, purple"
    result = validate_color_code(input_code, valid_colors)
    assert result == False, "Expected False for input of 4 colors where 3 are valid and 1 is invalid"

#write a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where 2 are valid and 2 are invalid
def test_validate_color_code_boundary_case_half_valid_colors():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where 2 are valid and 2 are invalid
    input_code = "red, green, purple, orange"
    result = validate_color_code(input_code, valid_colors)
    assert result == False, "Expected False for input of 4 colors where 2 are valid and 2 are invalid"

#write a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where 1 is valid and 3 are invalid
def test_validate_color_code_boundary_case_one_valid_color():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where 1 is valid and 3 are invalid
    input_code = "red, purple, orange, pink"
    result = validate_color_code(input_code, valid_colors)
    assert result == False, "Expected False for input of 4 colors where 1 is valid and 3 are invalid"

#write a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where all of them are valid but they are in uppercase
def test_validate_color_code_boundary_case_uppercase_colors():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where all are valid but in uppercase
    input_code = "RED, GREEN, BLUE, YELLOW"
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of 4 valid colors in uppercase"

#write a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where all of them are valid but they have extra spaces around them
def test_validate_color_code_boundary_case_colors_with_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where all are valid but have extra spaces
    input_code = " red , green , blue , yellow "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of 4 valid colors with extra spaces"

#write a boundry test for the validate_color_code function in Logic.py that tests the input of 4 colors where all of them are valid but they are in uppercase and have extra spaces around them
def test_validate_color_code_boundary_case_uppercase_colors_with_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of 4 colors where all are valid but in uppercase and have extra spaces
    input_code = " RED , GREEN , BLUE , YELLOW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of 4 valid colors in uppercase with extra spaces"

#write a boundry test for the validate_color_code function in Logic.py that simulates an empty string as input
def test_validate_color_code_boundary_case_empty_string():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of an empty string
    input_code = ""
    result = validate_color_code(input_code, valid_colors)
    assert result == False, "Expected False for input of an empty string"



#write a boundry test for the compareGuess function in Logic.py that tests the input of a user guess that is completely incorrect (e.g. "purple, orange, pink, cyan" compared to "red, green, blue, yellow")
def test_compare_guess_boundary_case_completely_incorrect():
    user_guess = "purple, orange, pink, cyan"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 0 and partial == 0, "Expected 0 exact matches and 0 partial matches for a completely incorrect guess"

#write a boundry test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but in uppercase (e.g. "RED, GREEN, BLUE, YELLOW" compared to "red, green, blue, yellow")
def test_compare_guess_boundary_case_completely_correct_uppercase():
    user_guess = "RED, GREEN, BLUE, YELLOW"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess in uppercase"

#write a boundry test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but has extra spaces (e.g. " red , green , blue , yellow " compared to "red, green, blue, yellow")
def test_compare_guess_boundary_case_completely_correct_with_extra_spaces():
    user_guess = " red , green , blue , yellow "
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess with extra spaces"

#write a boundry test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but in uppercase and has extra spaces (e.g. " RED , GREEN , BLUE , YELLOW " compared to "red, green, blue, yellow")
def test_compare_guess_boundary_case_completely_correct_uppercase_with_extra_spaces():
    user_guess = " RED , GREEN , BLUE , YELLOW "
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess in uppercase with extra spaces"



#write a boundry test for the guessAlgorithm function in Logic.py that tests the input of an empty list of previous guesses and feedback (i.e. the bot's first guess)
def test_guess_algorithm_boundary_case_first_guess_empty_history():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    first_guess = guessAlgorithm([], [], 0)

    # Should return a 4-color guess
    assert isinstance(first_guess, list) and len(first_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in first_guess)

    # First guess should be two colors repeated twice (e.g. [a, a, b, b])
    assert len(set(first_guess)) == 2
    for color in set(first_guess):
        assert first_guess.count(color) == 2


#write a boundry test for the guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback where the feedback indicates that the bot has already guessed the correct code (e.g. feedback of (4, 0) for a previous guess)
def test_guess_algorithm_boundary_case_correct_code_already_guessed():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "green", "blue", "yellow"]
    ]
    feedback = [
        (4, 0)  # 4 correct positions, 0 correct colors wrong position (code already guessed)
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 1)

    # Should return a 4-color guess (the algorithm should still return a guess even if the code was already guessed)
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)


#write a boundry test for the guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback where the feedback indicates that the bot has not made any correct guesses yet (e.g. feedback of (0, 0) for all previous guesses)
def test_guess_algorithm_boundary_case_no_correct_guesses_yet():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "red", "red", "red"],
        ["green", "green", "green", "green"]
    ]
    feedback = [
        (0, 0),  # 0 correct positions, 0 correct colors wrong position
        (0, 0)   # 0 correct positions, 0 correct colors wrong position
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 2)

    # Should return a 4-color guess
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)


#write a boundry test for the cheaterCheck function in Logic.py that tests the input of feedback that is impossible given the bot's guess and the code (e.g. feedback of (4, 0) for a guess that does not match the code)
def test_cheater_check_boundary_case_impossible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "white"]

    feedback = (4, 0)
    result = cheaterCheck(feedback, bot_guess, code)

    assert isinstance(result, str) and "cheating" in result.lower(), "Expected a cheating detection message for impossible feedback"

#write a boundry test for the cheaterCheck function in Logic.py that tests the input of feedback that is possible given the bot's guess and the code (e.g. feedback of (2, 1) for a guess that has 2 colors in the correct position and 1 color in the wrong position)
def test_cheater_check_boundary_case_possible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "yellow", "white"]

    feedback = (2, 1)
    result = cheaterCheck(feedback, bot_guess, code)

    assert result is None, "Expected None for possible feedback"

#write a boundry test for the cheaterCheck function in Logic.py that tests the input of feedback that is on the boundary of being possible (e.g. feedback of (3, 1) for a guess that has 3 colors in the correct position and 1 color in the wrong position, which is possible but very unlikely)
def test_cheater_check_boundary_case_boundary_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "yellow"]
    
    # Feedback like (3, 1) is inconsistent in Mastermind scoring, so it should be flagged.
    feedback = (3, 1)  # 3 correct positions, 1 correct color wrong position
    
    result = cheaterCheck(feedback, bot_guess, code)
    
    assert isinstance(result, str) and "cheating" in result.lower(), "Expected a cheating detection message for inconsistent feedback"

#write a boundry test for the cheaterCheck function in Logic.py that tests the input of feedback that is on the boundary of being impossible (e.g. feedback of (4, 0) for a guess that has 3 colors in the correct position and 1 color in the wrong position, which is impossible)
def test_cheater_check_boundary_case_boundary_impossible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "white"]

    feedback = (4, 0)
    result = cheaterCheck(feedback, bot_guess, code)

    assert isinstance(result, str) and "cheating" in result.lower(), "Expected a cheating detection message for boundary impossible feedback"

"""Happy path tests"""


#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code (e.g. "red, green, blue, yellow")
def test_validate_color_code_happy_path():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code
    input_code = "red, green, blue, yellow"
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code"


#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with extra spaces (e.g. " red , green , blue , yellow ")
def test_validate_color_code_happy_path_with_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with extra spaces
    input_code = " red , green , blue , yellow "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with extra spaces"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code in uppercase (e.g. "RED, GREEN, BLUE, YELLOW")
def test_validate_color_code_happy_path_uppercase():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code in uppercase
    input_code = "RED, GREEN, BLUE, YELLOW"
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code in uppercase"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code in uppercase with extra spaces (e.g. " RED , GREEN , BLUE , YELLOW ")
def test_validate_color_code_happy_path_uppercase_with_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code in uppercase with extra spaces
    input_code = " RED , GREEN , BLUE , YELLOW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code in uppercase with extra spaces"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with mixed case and extra spaces (e.g. " ReD , GrEeN , BlUe , YeLLoW ")
def test_validate_color_code_happy_path_mixed_case_with_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with mixed case and extra spaces
    input_code = " ReD , GrEeN , BlUe , YeLLoW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with mixed case and extra spaces"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with mixed case (e.g. "ReD, GrEeN, BlUe, YeLLoW")
def test_validate_color_code_happy_path_mixed_case():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with mixed case
    input_code = "ReD, GrEeN, BlUe, YeLLoW"
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with mixed case"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with leading and trailing spaces (e.g. " red, green, blue, yellow ")
def test_validate_color_code_happy_path_with_leading_trailing_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with leading and trailing spaces
    input_code = " red, green, blue, yellow "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with leading and trailing spaces"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with leading and trailing spaces and mixed case (e.g. " ReD, GrEeN, BlUe, YeLLoW ")
def test_validate_color_code_happy_path_with_leading_trailing_spaces_and_mixed_case():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with leading and trailing spaces and mixed case
    input_code = " ReD, GrEeN, BlUe, YeLLoW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with leading and trailing spaces and mixed case"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with leading and trailing spaces and mixed case and extra spaces (e.g. " ReD , GrEeN , BlUe , YeLLoW ")
def test_validate_color_code_happy_path_with_leading_trailing_spaces_and_mixed_case_and_extra_spaces():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with leading and trailing spaces and mixed case and extra spaces
    input_code = " ReD , GrEeN , BlUe , YeLLoW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with leading and trailing spaces and mixed case and extra spaces"

#write a happy path test for the validate_color_code function in Logic.py that tests the input of a valid color code with leading and trailing spaces and mixed case and extra spaces and special characters (e.g. " ReD , GrEeN , BlUe , YeLLoW ")
def test_validate_color_code_happy_path_with_leading_trailing_spaces_and_mixed_case_and_extra_spaces_and_special_characters():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]
    
    # Test input of a valid color code with leading and trailing spaces and mixed case and extra spaces and special characters
    input_code = " ReD , GrEeN , BlUe , YeLLoW "
    result = validate_color_code(input_code, valid_colors)
    assert result == True, "Expected True for input of a valid color code with leading and trailing spaces and mixed case and extra spaces and special characters"

#write a happy path test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but has extra spaces (e.g. " red , green , blue , yellow " compared to "red, green, blue, yellow")
def test_compare_guess_happy_path_completely_correct_with_extra_spaces():
    user_guess = " red , green , blue , yellow "
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess with extra spaces"

#write a happy path test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but in uppercase and has extra spaces (e.g. " RED , GREEN , BLUE , YELLOW " compared to "red, green, blue, yellow")
def test_compare_guess_happy_path_completely_correct_uppercase_with_extra_spaces():
    user_guess = " RED , GREEN , BLUE , YELLOW "
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess in uppercase with extra spaces"

#write a happy path test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct but in uppercase (e.g. "RED, GREEN, BLUE, YELLOW" compared to "red, green, blue, yellow")
def test_compare_guess_happy_path_completely_correct_uppercase():
    user_guess = "RED, GREEN, BLUE, YELLOW"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess in uppercase"

#write a happy path test for the compareGuess function in Logic.py that tests the input of a user guess that is completely correct (e.g. "red, green, blue, yellow" compared to "red, green, blue, yellow")
def test_compare_guess_happy_path_completely_correct():
    user_guess = "red, green, blue, yellow"
    generated_code = "red, green, blue, yellow"
    
    exact, partial = compareGuess(user_guess, generated_code)
    
    assert exact == 4 and partial == 0, "Expected 4 exact matches and 0 partial matches for a completely correct guess"
    
#write a happy path test for the guessAlgorithm function in Logic.py that tests the input of an empty list of previous guesses and feedback (i.e. the bot's first guess)
def test_guess_algorithm_happy_path_first_guess_empty_history():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    first_guess = guessAlgorithm([], [], 0)

    # Should return a 4-color guess
    assert isinstance(first_guess, list) and len(first_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in first_guess)

    # First guess should be two colors repeated twice (e.g. [a, a, b, b])
    assert len(set(first_guess)) == 2
    for color in set(first_guess):
        assert first_guess.count(color) == 2

#write a happy path test for the guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback where the feedback indicates that the bot has not made any correct guesses yet (e.g. feedback of (0, 0) for all previous guesses)
def test_guess_algorithm_happy_path_no_correct_guesses_yet():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "red", "red", "red"],
        ["green", "green", "green", "green"]
    ]
    feedback = [
        (0, 0),  # 0 correct positions, 0 correct colors wrong position
        (0, 0)   # 0 correct positions, 0 correct colors wrong position
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 2)

    # Should return a 4-color guess
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)

#write a happy path test for the guessAlgorithm function in Logic.py that tests the input of a non-empty list of previous guesses and feedback where the feedback indicates that the bot has already guessed the correct code (e.g. feedback of (4, 0) for a previous guess)
def test_guess_algorithm_happy_path_correct_code_already_guessed():
    valid_colors = ["green", "red", "yellow", "blue", "white", "black"]

    previous_guesses = [
        ["red", "green", "blue", "yellow"]
    ]
    feedback = [
        (4, 0)  # 4 correct positions, 0 correct colors wrong position (code already guessed)
    ]

    next_guess = guessAlgorithm(previous_guesses, feedback, 1)

    # Should return a 4-color guess (the algorithm should still return a guess even if the code was already guessed)
    assert isinstance(next_guess, list) and len(next_guess) == 4

    # All guessed colors should be valid
    assert all(color in valid_colors for color in next_guess)


#write a happy path test for the cheaterCheck function in Logic.py that tests the input of feedback that is possible given the bot's guess and the code (e.g. feedback of (2, 1) for a guess that has 2 colors in the correct position and 1 color in the wrong position)
def test_cheater_check_happy_path_possible_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "yellow", "white"]

    feedback = (2, 1)
    result = cheaterCheck(feedback, bot_guess, code)

    assert result is None, "Expected None for possible feedback"

#write a happy path test for the cheaterCheck function in Logic.py that tests the input of feedback that is on the boundary of being possible (e.g. feedback of (3, 1) for a guess that has 3 colors in the correct position and 1 color in the wrong position, which is possible but very unlikely)
def test_cheater_check_happy_path_boundary_feedback():
    bot_guess = ["red", "green", "blue", "yellow"]
    code = ["red", "green", "blue", "white"]

    # Boundary-ish valid feedback: 3 exact matches, 0 partial.
    feedback = (3, 0)

    result = cheaterCheck(feedback, bot_guess, code)

    assert result is None, "Expected None for valid feedback"