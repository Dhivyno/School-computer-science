names = []
shots = []
assists = []
goals = []
successlist = []
total = 0
 
for i in range(30):
 name = input("Input a name:  ")
 names.append(name)
 shotnum = int(input("Enter the number of the player's shots:  "))
 while shotnum > 100:
   shotnum = int(input("The maximum number of shots is 100. Enter a valid number:  "))
 shots.append(shotnum)
 assistnum = int(input("Enter the number of the player's assists:  "))
 while assistnum > 50:
   assistnum = int(input("The maximum number of assists is 50. Enter a valid number:  "))
 assists.append(assistnum)
 goalnum = int(input("Enter the number of the player's goals:  "))
 while goalnum > 40:
   goalnum = int(input("The maximum number of goals is 40. Enter a valid number:  "))
 goals.append(goalnum)
