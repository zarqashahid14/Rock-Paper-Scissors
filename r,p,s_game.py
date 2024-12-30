import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ").lower()


    if user_choice == 'r':
        user_choice = "rock"
    elif user_choice == 'p':
        user_choice = "paper"
    elif user_choice == 's':
        user_choice = "scissors"
    else:
        print("Invalid Choice. Please Try Again!")
        continue


    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You Win!")
    else:
        print("Computer Wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break