# wyrdle.py

import pathlib
import random

def get_random_word():
    
    WORDLIST = pathlib.Path("wordlist.txt")

    words = [
        word.upper()
        for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
    ]
    word = random.choice(words)
    print(f"Secret word is {word}")
    return word
    
def show_guess():

    for guess_count in range(1,7):
        guess = input(f"\nGuess {guess_count}: ").upper()
        if guess == word:
            print("correct")
            break
    
    correct_letters = { letter for letter, correct in zip(guess, word) if letter == correct }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct Letters:", ", ".join(correct_letters))
    print("Misplaced Letters:", ", ".join(misplaced_letters))
    print("Wrong Letters:", ", ".join(wrong_letters))
    
def end_game():
    
    print(f"Secret word was {word}")

def main()
    
    #Pre-Process
    get_random_word()
    
    #Main Process
    show_guess()

    #Post-Process
    end_game()

if __name__ == '__main__':
    main()
