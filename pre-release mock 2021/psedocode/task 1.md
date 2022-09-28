bid_number ← 0
INPUT “How many items do you have for auctioning?  ”, item_counter
WHILE item_counter < 10:
    INPUT “You need at least 10 items to auction, plz try again  ”, item_counter
ENDWHILE
FOR i ← 1 TO item_counter
    INPUT “What is the item number of the item you want to add?  ”, number
    WHILE LEN(number) != 3 OR number < 0
        INPUT “please input a valid 3 digit positive integer:  ”, number
    ENDWHILE
    item_numbers[item_counter] ← number
    INPUT “What is the description of the item you want to add?  ”, item_des
    WHILE LEN(item_des) < 10
        INPUT “the description has to be at least 10 characters long”, item_des
    ENDWHILE         
    descriptions[item_counter] ← item_des
    INPUT “What is the lowest price that you are willing to sell this item?  ”, price
    WHILE price < 0: 
        INPUT “please enter a valid positive integer”, price
    ENDWHILE
    reserve_price[item_counter] ← price
NEXT i
FOR i ← 1 TO item _counter
    OUTPUT "item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i]
NEXT i
