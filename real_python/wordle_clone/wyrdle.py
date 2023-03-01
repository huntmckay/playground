# wyrdle.py

for guess_count in range(1,7):
    word = "SNAKE"
    guess = input(f"\nGuess {guess_count}: ").upper()
    correct_letters = set(word) & set(guess)
    #misplaced_letters = 
    wrong_letters = set(word) - set(guess)
    print(f"The correct letters are {correct_letters}")
    print(f"The wrong letters are {wrong_letters}")
    if guess == word:
        print("correct")
        break

    print("wrong")
