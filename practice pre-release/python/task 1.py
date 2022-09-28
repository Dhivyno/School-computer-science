Wins = []
player1_wins = 0
player2_wins = 0
player1 = []
player2 = []
for i in range(30):
 player1_choice = input("enter player 1’s choice:  ")
 while player1_choice not in ["rock", "paper", "scissors"]:
   player1_choice = input("that is not an option, please try again:  ")
 player2_choice = input("enter player 2’s choice:  ")
 while player2_choice not in ["rock", "paper", "scissors"]:
   player2_choice = input("that is not an option, please try again:  ")
