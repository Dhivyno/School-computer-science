import random
menu_question = int(input("Type 1 if you want to play against computer and 2 if you want to play multiplayer and if you want a randomly chosen answer given to you, type 3:"))
 
if menu_question == 2:
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
 
 
if menu_question == 1:
 choice_list = ["rock", "paper", "scissors"]
 Wins = []
 comp_wins = 0
 player_wins = 0
 comp = []
 player = []
 print("First, let me give you some advice from a wise old man. he said, if you are calm and composed pick rock, if you are thin and weak pick paper, if you are mad with rage and want revenge pick scissors")
 for i in range(30):
   comp_choice = random.choice(choice_list)
   player_choice = input("enter player's choice:  ")
   while player_choice not in ["rock", "paper", "scissors"]:
     player_choice = input("that is not an option, please try again:  ")
   if comp_choice == "rock" and player_choice == "scissors":
     Wins.append("comp")
   if comp_choice == "rock" and player_choice == "paper":
     Wins.append("player")
   if comp_choice == "rock" and player_choice == "rock":
     Wins.append("both players because they drew")
   if comp_choice == "scissors" and player_choice == "scissors":
     Wins.append("both players because they drew")
   if comp_choice == "scissors" and player_choice == "paper":
     Wins.append("comp")
   if comp_choice == "scissors" and player_choice == "rock":
     Wins.append("player")
   if comp_choice == "paper" and player_choice == "scissors":
     Wins.append("player")
   if comp_choice == "paper" and player_choice == "paper":
     Wins.append("both players because they drew")
   if comp_choice == "paper" and player_choice == "rock":
     Wins.append("comp")
   print("the winner is", Wins[i], "with", comp_choice, "against", player_choice)
   if Wins[i] == "comp":
     comp_wins += 1
   if Wins[i] == "player":
     player_wins += 1
 if comp_wins > player_wins:
   print("comp won overall with", comp_wins, "wins")
 if comp_wins < player_wins:
   print("player won overall with", player_wins, "wins")
 if comp_wins == player_wins:
   print("it's a tie overall")
 
 
if menu_question == 3:
 choice_list = ["rock", "paper", "scissors"]
 Wins = []
 comp_wins = 0
 player_wins = 0
 comp = []
 player = []
 for i in range(30):
   comp_choice = random.choice(choice_list)
   player_choice = random.choice(choice_list)
   if comp_choice == "rock" and player_choice == "scissors":
     Wins.append("comp")
   if comp_choice == "rock" and player_choice == "paper":
     Wins.append("player")
   if comp_choice == "rock" and player_choice == "rock":
     Wins.append("both players because they drew")
   if comp_choice == "scissors" and player_choice == "scissors":
     Wins.append("both players because they drew")
   if comp_choice == "scissors" and player_choice == "paper":
     Wins.append("comp")
   if comp_choice == "scissors" and player_choice == "rock":
     Wins.append("player")
   if comp_choice == "paper" and player_choice == "scissors":
     Wins.append("player")
   if comp_choice == "paper" and player_choice == "paper":
     Wins.append("both players because they drew")
   if comp_choice == "paper" and player_choice == "rock":
     Wins.append("comp")
   print("the winner is", Wins[i], "with", comp_choice, "against", player_choice)
   if Wins[i] == "comp":
     comp_wins += 1
   if Wins[i] == "player":
     player_wins += 1
 if comp_wins > player_wins:
   print("comp won overall with", comp_wins, "wins")
 if comp_wins < player_wins:
   print("player won overall with", player_wins, "wins")
 if comp_wins == player_wins:
   print("it's a tie overall")
