#Rock, Paper, Scissors game
import random

choices = ["rock", "paper", "scissors"]
# This dictionary maps the winner to the loser: {Winner: Loser}
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

print("Rock, Paper, Scissors! (Type 'exit' to stop)")

while True:
    user = input("\nYour move: ").lower()
    if user == "exit": break
    if user not in choices: continue

    cpu = random.choice(choices)
    print(f"Computer: {cpu}")

    if user == cpu:
        print("Tie!")
    elif beats[user] == cpu:
        print("You Win! ✨")
    else:
        print("You Lose! 💀")
