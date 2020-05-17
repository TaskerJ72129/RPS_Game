import random
rps = input("Please choose rock (r), paper (p), or scissors (s): ")

computer_choice = ["rock", "paper", "scissors"]
chosen = random.choice(computer_choice)
print("User: {}     |     Computer: {}     |     Result: {}".format(rps, computer_choice, result))
