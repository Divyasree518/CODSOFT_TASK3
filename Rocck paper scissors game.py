import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")
print("Instructions:")
print("- Type Rock, Paper, or Scissors")
print("- Type 'exit' anytime to quit\n")
while True:
    user_choice = input("Enter your choice: ").lower()
    if user_choice == "exit":
        break
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.\n")
        continue
    computer_choice = random.choice(choices)
    print(f"\nYou chose      : {user_choice.capitalize()}")
    print(f"Computer chose : {computer_choice.capitalize()}")
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💻 Computer Wins!")
        computer_score += 1
    print("\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("\n===================================")
print("        FINAL SCORE")
print("===================================")
print(f"You      : {user_score}")
print(f"Computer : {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You won the game.")
elif computer_score > user_score:
    print("💻 Computer won the game.")
else:
    print("🤝 The game ended in a tie.")

print("\nThank you for playing!")
