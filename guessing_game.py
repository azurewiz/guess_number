import random
import time

# Dictionary to store high scores for each difficulty level
# Stores the minimum attempts taken to win
high_scores = {
    "Easy": float('inf'),
    "Medium": float('inf'),
    "Hard": float('inf')
}

def get_difficulty():
    """Prompts the user to select a difficulty level and returns the level name and chances."""
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
            return "Easy", 10
        elif choice == '2':
            return "Medium", 5
        elif choice == '3':
            return "Hard", 3
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def give_hint(secret_number, guess):
    """Provides a smart hint based on the secret number and the user's incorrect guess."""
    hints = []
    # Hint 1: Even or Odd
    if secret_number % 2 == 0:
        hints.append("The secret number is Even.")
    else:
        hints.append("The secret number is Odd.")
        
    # Hint 2: Range proximity
    diff = abs(secret_number - guess)
    if diff <= 5:
        hints.append("You are burning hot! (Within 5 numbers)")
    elif diff <= 15:
        hints.append("You are getting warm! (Within 15 numbers)")
        
    return random.choice(hints)

def play_round():
    """Handles a single round of the number guessing game."""
    global high_scores
    
    print("\n" + "="*40)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("="*40)
    
    difficulty_name, total_chances = get_difficulty()
    print(f"\nGreat! You have selected the {difficulty_name} difficulty level.")
    print("Let's start the game!")
    
    # Setup game state
    secret_number = random.randint(1, 100)
    chances_left = total_chances
    attempts = 0
    start_time = time.time()
    
    while chances_left > 0:
        print(f"\nChances remaining: {chances_left}")
        user_input = input("Enter your guess (or type 'hint' for a clue): ").strip().lower()
        
        # Handle hint request
        if user_input == 'hint':
            if attempts == 0:
                print("💡 Take at least one guess before asking for a hint!")
            else:
                print(f"💡 HINT: {give_hint(secret_number, last_guess)}")
            continue
            
        # Validate numeric input
        try:
            guess = int(user_input)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'hint'.")
            continue
            
        # Track valid attempt
        attempts += 1
        chances_left -= 1
        last_guess = guess
        
        # Check Win/Loss conditions
        if guess == secret_number:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            
            print(f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"⏱️ Time taken: {duration} seconds.")
            
            # Update high score
            if attempts < high_scores[difficulty_name]:
                high_scores[difficulty_name] = attempts
                print(f"🏆 New High Score for {difficulty_name} difficulty!")
            else:
                print(f"Current High Score for {difficulty_name}: {high_scores[difficulty_name]} attempts.")
            return
            
        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")
            
    # Out of chances
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"\n💥 Game Over! You've run out of chances.")
    print(f"The correct number was: {secret_number}")
    print(f"⏱️ Time survived: {duration} seconds.")

def main():
    """Main loop to handle replay functionality."""
    while True:
        play_round()
        
        # Ask to play again
        print("\n" + "-"*40)
        replay = input("Do you want to play another round? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\nThanks for playing! Final High Scores:")
            for level, score in high_scores.items():
                score_str = f"{score} attempts" if score != float('inf') else "No wins yet"
                print(f" - {level}: {score_str}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()