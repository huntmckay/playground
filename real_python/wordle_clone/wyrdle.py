# wyrdle.py

WORD = "SNAKE"

for guess_count in range(1,7):
    guess = input(f"\nGuess {guess_count}: ").upper()
    if guess == WORD:
        print("correct")
        break


    correct_letters = { letter for letter, correct in zip(guess, WORD) if letter == correct }

    misplaced_letters = set(guess) & set(WORD) - correct_letters

    wrong_letters = set(guess) - set(WORD)

    print("Correct Letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced Letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrongn Letters:", ", ".join(sorted(wrong_letters)))
