discount ← 0
multiplier ← 5
checksum ← 0
INPUT “What day are you parking your car?”, str, arrivalday
WHILE arrivalday NOT IN ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] DO
 INPUT “Invalid day. Please enter a valid day”, str, arrivalday
ENDWHILE
INPUT "What time did you arrive? (No minutes Examples: 15:45 is 15 and midnight is 0)   ", int, arrivaltime
WHILE arrivaltime < 8 or arrivaltime > 23 DO
 INPUT "Invalid arrival time, please enter a valid arrival time between 8 and 23: ", int, arrivaltime
ENDWHILE
INPUT "How many hours are you parking the vehicle for? ", int, parkingtime
 
REPEAT
 IF arrivaltime >= 8 AND arrivaltime < 16
   THEN IF arrivalday = "sunday" AND parkingtime > 8
     THEN INPUT "8 is the maximum hours that you can park on Sunday. Please enter a valid number of hours to park: ", int, parkingtime
   ELIF arrivalday = "saturday" and parkingtime > 4
     THEN INPUT "4 is the maximum hours that you can park on Saturday. Please enter a valid number of hours to park: ", int, parkingtime
   ELIF parkingtime > 2 and arrivalday != "sunday" and arrivalday != "saturday"
     THEN INPUT "2 is the maximum number of hours you can park on weekdays. Please enter a valid number of hours to park: ", int, parkingtime
   ELSE
     breakbool = 1
 ELSE
   IF arrivaltime + parkingtime > 24:
     THEN INPUT "You can only park until midnight. Please enter a valid number of hours to park: ", int, parkingtime
   ELSE
     breakbool = 1
UNTIL breakbool = 1
 
INPUT "If you have a frequent parking number, please enter it here. If you don't have one, enter No", str, frequentnumber
IF frequentnumber IN ["no", "No"]
 THEN discount ← 0
ELSE
 FOR i in 0 to 4 DO
   checksum ← multiplier*int(frequentnumber[i]) + checksum
   multiplier ← multiplier - 1
 sumdiv ← 11 - checksum%11
 IF sumdiv = int(frequentnumber[4])
   THEN discount ← 1
 NEXT i

IF arrivalday = “sunday” AND arrivaltime + parkingtime < 17
	THEN price ← parkingtime*2
ELSEIF arrivaltime + parkingtime < 17
  IF arrivalday = "saturday"
    THEN price ←  parkingtime*3
  IF arrivalday != "saturday" AND arrivalday != "sunday"
    THEN price ←  parkingtime*10
ELSEIF arrivaltime >= 17
  THEN price ← 2*parkingtime 
ELSE
  IF arrivalday = "sunday":
    THEN price ← 2*(16-arrivaltime) + 2
  IF arrivalday = "saturday":
    THEN price ← 3*(16-arrivaltime) + 2
  IF arrivalday != "saturday" AND arrivalday != "sunday":
    THEN price ← 10*(16-arrivaltime) + 2
