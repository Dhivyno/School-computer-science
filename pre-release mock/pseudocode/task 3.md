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
