import random

def get_player_choice() -> str:
    choices = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        choice = input("Choose [R]ock, [P]aper, or [S]cissors: ").strip().lower()
        if choice in choices:
            return choices[choice]
        if choice in choices.values():
            return choice
        print("Invalid choice. Please enter R, P, S, rock, paper, or scissors.")


def get_computer_choice() -> str:
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player: str, computer: str) -> str:
    if player == computer:
        return "tie"

    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    return "player" if wins[player] == computer else "computer"


def main() -> None:
    print("Welcome to Rock Paper Scissors!")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
        else:
            print("Computer wins!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
