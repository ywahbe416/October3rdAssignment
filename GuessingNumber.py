# Guessing game that allows players to guess a number between 1 and a 100
import random
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10


print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("After each guess, you'll get a hint if your guess is too high or too low.")
print("You have a maximum of 10 attempts to guesss.")

while attempts < max_attempts:
    try:
            guess = int(input("Enter your guess: "))
    except ValueError:
            print("Please enter a valid integer.")
            continue
    attempts += 1
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!")
