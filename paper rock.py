import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"
    else:
        return "Invalid choice."

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        print("\nRock, Paper, Scissors")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice_num = input("Enter your choice (1/2/3): ")
        if user_choice_num not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            continue

        user_choice = choices[int(user_choice_num) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "tie" not in result:
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == 'yes'

if __name__ == "__main__":
    play_game()
