#Rock paper scissors component 1 Input

# To do
# - Give user choice between RPS or RPSLS
# - Depending on users choice prior ask them what attack they would like to choose
# - Ask user best out of ?

# Functions go here
def intcheck(question,low):
    while True:
        try:
            response = int(input(question))
            if response < low:
                print("Please enter a whole number above 0")
                continue
            return response
        except ValueError:
            print("Please enter a whole number above 0")


# Main code
rps_valid = False
while not rps_valid:

    rps = input("Please choose from Rock(R), Paper(P) or Scissors(S): ").lower()

    if rps == "r" or rps == "rock":
        rps_choice = "rock"
    elif rps == "p" or rps == "paper":
        rps_choice = "paper"
    elif rps == "s" or rps == "scissors":
        rps_choice = "scissors"

    else:
        continue
    print(rps_choice)
    rps_valid = True

rounds_valid = False
while not rounds_valid:
    rounds = intcheck("How many rounds ?", 1)
    if rounds % 2 == 0:
        print("Please enter an odd number above 0")
        continue
    rounds_valid = True
