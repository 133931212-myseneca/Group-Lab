# OPS445 GROUP LAB

## Students participating:
Madhav Uppal - 133931212
Devank - 153322219
Mohit Kumar - 123049215

### What is Rock-Paper-Scissors game?
"Rock, Paper, Scissors" is a game where you face the computer. Choose "rock," "paper," or "scissors." The computer also chooses. Rock beats scissors, scissors beats paper, paper beats rock. The winner is declared, and you can play again or quit. The game continues until you decide to stop.

### Instructions on how to play the game:
```
Start the Game with the command:
python3 ./rock_paper_scissors.py

Run the program to start the Rock, Paper, Scissors game.

Game Introduction:
The game will display a welcome message: "Welcome to Rock, Paper, Scissors!"

Player's Turn:
You are the player. You'll be prompted to input your choice by typing "rock", "paper", or "scissors" (without quotes). Type your choice and press Enter. Your input is case-insensitive, so it can be in uppercase or lowercase.

Computer's Turn:
The computer will randomly select one of the three options: "rock", "paper", or "scissors".

Display Choices:
The game will display both your choice and the computer's choice. For example:

Computer chose: rock
You chose: scissors

Determine the Winner:
The game will compare your choice and the computer's choice to determine the winner:

If both choices are the same, the game declares it as a tie.

If you chose "rock" and the computer chose "scissors", you win.
If you chose "paper" and the computer chose "rock", you win.
If you chose "scissors" and the computer chose "paper", you win.

If none of the above conditions are met, the computer wins.

Announce the Winner:
The game will announce the winner of the round: "You win!" or "Computer wins!" or "It's a tie!"

Wanna Play Again?
After determining the winner, the game will ask if you want to play again: "Do you want to play again? (yes/no): "

If you want to play again, type "yes" and press Enter.
If you want to stop playing, type "no" and press Enter.

Repeat or End:
If you choose to play again, the game will start a new round.
If you choose not to play again, the game will end, and the program will exit.

End the Game:
The program will exit, and you'll have completed your Rock, Paper, Scissors gaming session.

Have fun playing!
```
### Algorithm:

```
Rock, Paper, Scissors Game

This is a simple implementation of the classic Rock, Paper, Scissors game. Players can choose one of three options (rock, paper, or scissors) to play against the computer's choice. The game continues until the player decides not to play again.

Players' Roles:
- Player: Chooses one of the three options (rock, paper, or scissors).
- Computer: Randomly selects one of the three options.

Algorithm:
1. Initialize the options list: ["rock", "paper", "scissors"]
2. Enter the game loop:
   a. Generate a random choice for the computer.
   b. Display the game welcome message.
   c. Prompt the player to input their choice (rock, paper, or scissors).
   d. Compare the player's choice with the computer's choice:
      - If they're the same, declare a tie.
      - Otherwise, check for win conditions:
         - Rock beats scissors.
         - Scissors beats paper.
         - Paper beats rock.
   e. Display the computer's choice and the game outcome.
   f. Ask the player if they want to play again.
      - If the player's answer is not 'yes', exit the loop.
3. End the game.
```

### Code for the Rock, Paper, Scissors game:

```
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

```
