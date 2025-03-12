import random
random_number = random.randint(1, 20)
guess_count = 0
max_attempts = 5

print("Guess a number between 1 and 20. You have 5 attempts.\n")

while guess_count < max_attempts:
    try:
        guess = int(input(f"Attempt {guess_count + 1}: Enter your guess: "))

        if guess < 1 or guess > 20:
            print("Invalid input! Please enter a number between 1 and 20.\n")
            continue 
        guess_count += 1 
        if guess < random_number:
            print("Too Low!\n")
        elif guess > random_number:
            print("Too High!\n")
        else:
            print(f"Correct! You guessed it in {guess_count} attempts.\n")
            break 

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

if guess_count == max_attempts and guess != random_number:
    print(f"Game Over! The correct number was {random_number}.\n")

print("Thanks for playing")
