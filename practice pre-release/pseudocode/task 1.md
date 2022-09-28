FOR i <— 1 TO 31:
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
NEXT i 
