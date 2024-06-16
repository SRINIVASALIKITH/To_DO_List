import random
import time

def intro():
    print("What's your name?")
    player_name = input()  # Ask for the player's name
    print(f"{player_name}, let's play a game. I'm thinking of a number between 1 and 500.")
    time.sleep(0.5)
    print("Try to guess it!")

def pick(number, player_name):
    attempts = 0
    max_attempts = 10  # Number of allowed attempts

    while attempts < max_attempts:  # Allow up to max_attempts guesses
        time.sleep(0.25)
        guess_input = input("Enter your guess: ")
        try:
            guess = int(guess_input)  # Convert the input to an integer

            if 1 <= guess <= 500:  # Ensure the guess is within the range
                attempts += 1
                if attempts < max_attempts:
                    if guess < number:
                        print("Your guess is too low.")
                    elif guess > number:
                        print("Your guess is too high.")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try again!")
                if guess == number:
                    break  # Exit the loop if the guess is correct
            else:
                print("That number is out of range! Please guess between 1 and 500.")
                time.sleep(0.25)

        except ValueError:
            print(f"{guess_input} is not a valid number. Please enter a number.")

    if guess == number:
        print(f'Congratulations, {player_name}! You guessed the number in {attempts} attempts!')
    else:
        print(f'Sorry, {player_name}. The number I was thinking of was {number}.')

def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        number = random.randint(1, 500)  # Pick a random number between 1 and 500
        intro()
        player_name = input("Please enter your name: ")
        pick(number, player_name)
        print("Would you like to play again? (yes or no)")
        play_again = input()

if __name__ == "__main__":
    main()
