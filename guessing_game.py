
print("Try programiz.pro")
import random
import time

# Function to start a new game
def start_game():
    # Ask the player to choose a difficulty level
    print("Choose your difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    difficulty = input("Enter the difficulty level (1/2/3): ")
    
    # Set the range and number of attempts based on the chosen difficulty
    if difficulty == "1":
        low, high, max_attempts = 1, 50, 15
    elif difficulty == "2":
        low, high, max_attempts = 1, 100, 10
    elif difficulty == "3":
        low, high, max_attempts = 1, 200, 7
    else:
        print("Invalid choice! Setting to Medium by default.")
        low, high, max_attempts = 1, 100, 10
    
    # Generate a random number between low and high (inclusive)
    secret_number = random.randint(low, high)
    
    # Initialize the number of attempts
    attempts = 0
    start_time = time.time()  # Start the timer
    
    print(f"\nI'm thinking of a number between {low} and {high}. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        # Get the player's guess
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        attempts += 1

        # Check the player's guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # End the timer and display the result
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            print(f"Time taken: {elapsed_time} seconds.")
            break  # Exit the loop if the guess is correct

        # Give a hint after half of the attempts
        if attempts >= max_attempts // 2:
            if secret_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
        
        # If maximum attempts are reached, tell the player and exit
        if attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    
    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        start_game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
start_game()
