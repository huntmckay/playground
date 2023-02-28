# wyrdle.py


guess_count = 0

while guess_count <= 4:
    guess = input("Guess a word: ").upper()
    if guess == "SNAKE":
        print("correct")
        break
    else:
        print("wrong")
        guess_count = guess_count +1
    print(guess_count)
