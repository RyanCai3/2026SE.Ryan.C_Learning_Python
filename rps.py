def main():
    player_choice()

def player_username():
    input("Enter player username: ")

def player_choice():
    player_choice = input(f"Hello {player_username}, enter your choice: ")

    match player_choice:
        case "scissors" | "paper" | "rock":
            print(f"You have chosen {player_choice}")
        case _:
            print("Choice unavailable")

def cpu_choice():
    print("Your opponent has chosen", )

main()