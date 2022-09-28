discount = 0
multiplier = 5
checksum = 0
arrivalday = input("What day are you parking your car? ")
while arrivalday not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
 arrivalday = input("Invalid day. Please enter a valid day: ")
arrivaltime = int(input("What time did you arrive? (No minutes Examples: 15:45 is 15 and midnight is 0)   "))
while arrivaltime < 8 or arrivaltime > 23:
 arrivaltime = int(input("Invalid arrival time, please enter a valid arrival time between 8 and 23: "))
parkingtime = int(input("How many hours are you parking the vehicle for? "))
 
while True:
 if arrivaltime >= 8 and arrivaltime < 16:
   if arrivalday == "sunday" and parkingtime > 8:
     parkingtime = int(input("8 is the maximum hours that you can park on Sunday. Please enter a valid number of hours to park: "))
   elif arrivalday == "saturday" and parkingtime > 4:
     parkingtime = int(input("4 is the maximum hours that you can park on Saturday. Please enter a valid number of hours t park: "))
   elif parkingtime > 2 and arrivalday != "sunday" and arrivalday != "saturday":
     parkingtime = int(input("2 is the maximum number of hours you can park on weekdays. Please enter a valid number of hours to park: "))
   else:
     break
 else:
   if arrivaltime + parkingtime > 24:
     parkingtime = int(input("You can only park until midnight. Please enter a valid number of hours to park: "))
   else:
     break
frequentnumber = str(input("If you have a frequent parking number, please enter it here. If you don't have one, enter No"))
if frequentnumber in ["no", "No"]:
 discount = 0
else:
 for i in range(4):
   checksum += multiplier*int(frequentnumber[i])
   multiplier -= 1
 sumdiv = 11 - checksum%11
 if sumdiv == int(frequentnumber[4]):
   discount = 1
 
if arrivalday == "sunday":
 price = parkingtime*2
elif arrivaltime + parkingtime < 17:
 if arrivalday == "saturday":
   price = parkingtime*3
 if arrivalday != "saturday" and arrivalday != "sunday":
   price = parkingtime*10
elif arrivaltime >= 17:
 price = 2*parkingtime
else:
 if arrivalday == "saturday":
   price = 3*(16-arrivaltime) + 2*(arrivaltime+parkingtime-16)
 if arrivalday != "saturday" and arrivalday != "sunday":
   price = 10*(16-arrivaltime) + 2*(arrivaltime+parkingtime-16)
 
if discount == 1 and arrivaltime >= 16 and arrivaltime < 24:
 print("The final price you have to pay is ", price/2, "for", parkingtime, "hours")
elif discount == 1 and arrivaltime >= 8 and arrivaltime < 16:
 print("The final price you have to pay is ", price*0.9, "for", parkingtime, "hours")
else:
 print("The final price you have to pay is ", price, "for", parkingtime, "hours")
