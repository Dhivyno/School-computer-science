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
 if player1_choice == "rock" and player2_choice == "scissors":
   Wins.append("player1")
 if player1_choice == "rock" and player2_choice == "paper":
   Wins.append("player2")
 if player1_choice == "rock" and player2_choice == "rock":
   Wins.append("both players because they drew")
 if player1_choice == "scissors" and player2_choice == "scissors":
   Wins.append("both players because they drew")
 if player1_choice == "scissors" and player2_choice == "paper":
   Wins.append("player1")
 if player1_choice == "scissors" and player2_choice == "rock":
   Wins.append("player2")
 if player1_choice == "paper" and player2_choice == "scissors":
   Wins.append("player2")
 if player1_choice == "paper" and player2_choice == "paper":
   Wins.append("both players because they drew")
 if player1_choice == "paper" and player2_choice == "rock":
   Wins.append("player1")
 print("the winner is", Wins[i], "with", player1_choice, "against", player2_choice)
 if Wins[i] == "player1":
   player1_wins += 1
 if Wins[i] == "player2":
   player2_wins += 1
if player1_wins > player2_wins:
 print("player1 won overall with", player1_wins, "wins")
if player1_wins < player2_wins:
 print("player2 won overall with", player2_wins, "wins")
if player1_wins == player2_wins:
 print("it's a tie overall")
