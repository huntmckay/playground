# wyrdle.py

import pathlib
import random
from string import ascii_letters

def get_random_word():
    
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)
    
def show_guess(guess,word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """

    if guess == word:
        return True
    else:
        correct_letters = { letter for letter, correct in zip(guess, word) if letter == correct }
        misplaced_letters = set(guess) & set(word) - correct_letters
        wrong_letters = set(guess) - set(word)

        print("Correct Letters:", ", ".join(correct_letters))
        print("Misplaced Letters:", ", ".join(misplaced_letters))
        print("Wrong Letters:", ", ".join(wrong_letters))
        
def end_game(word,win):
    
    if win:
        print(f"CORRECT! The Secret word was {word}")
    else:
        print(f"LOSER! The Secret word was {word}")

def main():
    
    #Pre-Process
    word = get_random_word()
    assert type(word) is str
    assert len(word) == 5

    print(f"Secret word is {word}")

    #Main Process
    for guess_count in range(1,7):
        guess = input(f"\nGuess {guess_count}: ").upper()
        if show_guess(guess,word):
            end_game(word,win=True)
            break

    #Post-Process
    else:
        end_game(word,win=False)

if __name__ == '__main__':
    main()
