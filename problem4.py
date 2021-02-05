import random

MIN = 1
MAX = 100
MAX_ATTEMPTS = 5


def guess_the_number():
    print(f"I'm thinking of a number between {MIN} and {MAX}.")
    answer = random.randint(MIN, MAX)
    guess = 0
    attempts = 0
    while guess != answer and attempts < MAX_ATTEMPTS:
        guess = int(input("Guess the number: "))
        if guess > answer:
            print("Too High.")
        elif guess < answer:
            print("Too Low.")
        attempts += 1

    if guess == answer:
        print(f"You got it! The answer was {answer}")
    else:
        print(f"Sorry, you've run out of attempts! The correct answer was {answer}")


guess_the_number()
