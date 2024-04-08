import random

def guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Guessing Game!")
    print("I've chosen a secret number between 1 and 10.")
    print("You have 3 attempts to guess the number. Good luck!\n")

    # Loop for the number of attempts
    for attempt in range(1, attempts + 1):
        guess = int(input("Attempt {}: Enter your guess: ".format(attempt)))

        # Check if the guess is correct, too high, or too low
        if guess == secret_number:
            print("Congratulations! You guessed the secret number!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    else:
        print("Sorry, you've run out of attempts. The secret number was {}.".format(secret_number))

# Call the function to start the game
guessing_game()
