import random
def snake_Water_Gun(player,computer):
    if computer == player:
        return "It's a tie!"
    elif (computer == "snake" and player == "water") or \
         (computer == "water" and player == "gun") or \
         (computer == "gun" and player == "snake"):
        return "You lose!"
    else:
        return "You win!"
print("Welcome to Snake Water Gun Game!")
choices = ["snake", "water", "gun"]
player_choice = input("Enter your choice (snake/water/gun): ").lower()
if player_choice not in choices:
    print("Invalid choice! Please choose from snake, water, or gun.")
    
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")
print(f"Your choice: {player_choice}")
    
result = snake_Water_Gun(player_choice, computer_choice)
print(result)
    
    