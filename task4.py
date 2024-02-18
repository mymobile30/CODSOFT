mport random

def win(user,comp):
    if user == comp:
        return "Tie "
    elif((user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper")):
        return " you are the  winner "
    else:
        return " computer wins " 

def game():
    print("Welcome to ROCK ,PAPER ,SCISSORS GAME ")
    user =input("Enter  your choice rock ,paper ,scissors : ").lower()
    if user not in ["rock","paper","scissors"]:
        print("invalid input .please choice choose rock or paper or scissors " )
        return
    comp = random.choice(["rock","paper","scissors"])
    print("your choice : ",user)
    print("computer choice : ",comp)

    winner=win(user,comp)
    print(winner)


game()
while True:
    replay=input("if you want to play again say YES OR NO :").lower()
    if replay != "yes" :
        print("Congrats for playagin the game : ")
        break
    game()
