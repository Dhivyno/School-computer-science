item_number = []
description = []
reserve_price = []
bid_number = []
highest_bid_list = []
buyer_number_list = []
removal_numbers = []
 
 
item_counter = int(input("How many items do you have for auctioning?  "))
while item_counter < 10:
 item_counter = int(input("There has to be atleast 10 items to auction. please try again.  "))
for i in range(item_counter):
 try:
   number = int(input("what is the item number of the item you want to add?  "))
 except:
   number = input("please verify the item number a second time:  ")
 while isinstance(number, int) != True or len(str(number)) != 3:
   try:
     number = int(input("please enter a valid integer for item number:  "))
   except:
     number = input("please verify the item number a second time:  ")
 item_number.append(number)
 item_des = input("What is the name and description of the item with this item number?  ")
 while len(item_des) < 10:
   item_des = input("A description has to have at lease 10 characters long")
 description.append(item_des)
 try:
   price = int(input("what is the lowest that you are willing to sell the item?  "))
 except:
   price = input("what is the lowest that you are willing to sell the item?")
 while isinstance(price, int) != True:
   try:
     price = int(input("please enter a valid integer for reserve price:  "))
   except:
     price = input("please enter a valid integer for reserve price:  ")
 reserve_price.append(str(price))
 
for i in range(item_counter):
 print("item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i])
 verification = input("Is this information correct?    ")
 if verification in ["no", "n", "No", "NO", "N"]:
   removal_numbers.append(i)
for i in range(len(removal_numbers)):
 item_number.remove(item_number[removal_numbers[i]])
 description.remove(description[removal_numbers[i]])
 reserve_price.remove(reserve_price[removal_numbers[i]])
print("The unwanted items has been removed")
if len(item_number) < 10:
 print("you dont have 10 items in your auction and the program had ended. plz try again")
 exit()
for i in range(len(item_number)):
 bid_number.append(0)
 
for i in range(item_counter):
 print("item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i])
