import random

def rock_paper_scissors():
    while True:
        options = ["rock", "paper", "scissors"]
        computer_option = random.choice(options)

        print("Welcome to Rock, Paper, Scissors!")
        user_option = input("Enter your choice (rock, paper, or scissors): ").lower()

        print(f"Computer chose: {computer_option}")
        print(f"You chose: {user_option}")

        if user_option == computer_option:
            print("It's a tie!")
        elif user_option == "rock":
            if computer_option == "scissors":
                print("You win!")
            else:
                print("Computer wins!")
        elif user_option == "paper":
            if computer_option == "rock":
                print("You win!")
            else:
                print("Computer wins!")
        elif user_option == "scissors":
            if computer_option == "paper":
                print("You win!")
            else:
                print("Computer wins!")
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    rock_paper_scissors()
