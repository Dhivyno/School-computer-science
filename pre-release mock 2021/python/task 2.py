item_number = []
description = []
reserve_price = []
bid_number = []
highest_bid_list = []
buyer_number_list = []
removal_numbers = []
item_counter = 0
valid_bidder_numbers = []
 
 
valid_bidder_counter = int(input("How many bidder do you have in your auction?"))
for i in range(valid_bidder_counter):
 valid_bidder = int(input("What is the bidder number of the first bidder?  "))
 valid_bidder_numbers.append(valid_bidder)
def adding_items():
 item_counter = int(input("How many items do you have for auctioning?  "))
 while len(item_number) + item_counter < 10:
   item_counter = int(input("There has to be atleast 10 items to auction. please try again.  "))
 for i in range(item_counter):
   try:
     number = int(input("what is the item number of the item you want to add?  "))
   except:
     number = input("please verify the item number a second time:  ")
   while isinstance(number, int) != True:
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
     price = input("please verify the lowest price of this item:  ")
   while isinstance(price, int) != True:
     try:
       price = int(input("please enter a valid integer for reserve price:  "))
     except:
       price = input("please verify the lowest price of this item:  ")
   reserve_price.append(str(price))
 
 for i in range(len(item_number)):
   print("item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i])
   verification = input("Is this information correct?    ")
   if verification in ["no", "n", "No", "NO", "N"]:
     removal_numbers.append(i)
 for j in range(len(removal_numbers)):
   item_number.remove(item_number[removal_numbers[j]])
   description.remove(description[removal_numbers[j]])
   reserve_price.remove(reserve_price[removal_numbers[j]])
 
  
adding_items()
if len(item_number) < 10:
 print("you dont have 10 items in your auction and the program had ended. plz try again")
 exit()
print("The unwanted items has been removed")
for i in range(len(item_number)):
 bid_number.append(0)
 highest_bid_list.append(0)
 buyer_number_list.append(0)
 
 
while True:
 menu_question = input("Do you want to bid or add more auction items?   ")
 if menu_question in ['add', 'Add', 'ADD']:
   adding_items()
  
 if menu_question in ['bid', 'Bid', 'BID']:
   for i in range(len(item_number)):
     print("item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i])
   bid_choice = int(input("Which item would you like to look at?  "))
   index_element = item_number.index(bid_choice)
   print("item number -", item_number[index_element], ". Description -", description[index_element], ". Reserve price is", reserve_price[index_element], "The current highest bid is", highest_bid_list[index_element])
   bid_yesorno = input("Do you want to bid for this item?  ")
   if bid_yesorno in ['yes', 'Yes', 'y', 'Y', 'YES']:
     bid_number[index_element] += 1
     bid_amount = int(input("What is the amount you want to bid for this item in dollars?  "))
     if int(highest_bid_list[index_element]) < bid_amount:
       bidder_number = int(input("What is your bidder number?  "))
       if bidder_number in valid_bidder_numbers:
         buyer_number_list[index_element] = bidder_number
         highest_bid_list[index_element] = bid_amount
       else:
         print("Your bidder number is not valid")
     else:
       print("Your bid has to be higher than the current highest bid, please try again")
      
 if menu_question in ['end', 'End', 'END']:
   exit()
