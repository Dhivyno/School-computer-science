FOR i <— 1 TO 31
    INPUT “enter player 1’s choice”, player1_choice 
    WHILE player1_choice NOT IN [“rock”, “paper”, “scissors”]
        INPUT “that is not an option, please try again”, player1_choice
    ENDWHILE
    INPUT “enter player 2’s choice”, player2_choice 
    WHILE player1_choice NOT IN [“rock”, “paper”, “scissors”]
        INPUT “that is not an option, please try again”, player2_choice
    ENDWHILE

    Player1[30] <— player1_choice
    Player2[30] <— player2_choice
    IF player1_choice = “rock” AND player2_choice = “scissors”
        Wins[30] <— “player1”
        Wins1 += 1 
    IF player1_choice = “rock” AND player2_choice = “paper”
        Wins[30] <— “player2”
        Wins2 += 1
    IF player1_choice = “rock” AND player2_choice = “rock”
        Wins[30] <— “both players because they drew”
    IF player1_choice = “scissors” AND player2_choice = “scissors”
        Wins[30] <— “both players because they drew”
    IF player1_choice = “scissors” AND player2_choice = “paper”
        Wins[30] <— “player1”
        Wins1 += 1 
    IF player1_choice = “scissors” AND player2_choice = “rock”
        Wins[30] <— “player2”
        Wins2 += 1
    IF player1_choice = “paper” AND player2_choice = “scissors”
        Wins[30] <— “player2”
        Wins2 += 1
    IF player1_choice = “paper” AND player2_choice = “paper”
        Wins[30] <— “both players because they drew”
    IF player1_choice = “paper” AND player2_choice = “rock”
        Wins[30] <— “player1”
        Wins1 += 1 
    OUTPUT “the winner is” Wins[i], “with”, player1_choice, “against”, player2_choice
    IF Wins1 > Wins2
        OUTPUT “player1 wins overall”
    IF Wins1 = Wins2
        OUTPUT “it’s a tie overall”
    ELSE
        OUTPUT “player2 wins overall”
