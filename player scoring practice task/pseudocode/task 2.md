squad_total← 0

FOR i ← 0-30
       INPUT name 
       names[i]  ← name
       INPUT shots : INTEGER
       WHILE shots >100 OR <0 DO
             OUTPUT “Invalid” 
             INPUT shots 
       INPUT assists: INTEGER
       WHILE assists >50 OR<0 DO 
             OUTPUT “Invalid”
             INPUT assists 
       INPUT goals : INTEGER
       WHILE goals >40 OR <0 DO 
             OUTPUT “Invalid”
             INPUT goals 
       squad_shots[i] ← shots
       squad_assists[i] ← assists
       squad_goals[i] ← goals
       success_index[i] ←  1*assists+2*shots+3*goals
       squad_total← squad_total+success_index[i] 
       OUTPUT name, success index[i]
NEXT

squad_average← squad_total/30
OUTPUT squad_average
