from wordle import Wordle
from letter_state import LetterState
import random
from typing import List
from colorama import Fore, Style

def main(): 
    word_set = load_word_set("wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    
    while wordle.can_attempt:
        x = input("Type your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!" + Style.RESET_ALL)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You have solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The word was {secret}")

def display_results(wordle: Wordle):
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Style.RESET_ALL
        result_with_color.append(colored_letter)
    return "".join(result_with_color)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

if __name__ == "__main__":
    main()
