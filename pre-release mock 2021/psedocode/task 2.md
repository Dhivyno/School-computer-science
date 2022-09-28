loop_constant = 0
bid_number ← 0
INPUT “How many items do you have for auctioning?  ”, item_counter
WHILE item_counter < 10
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
    WHILE price < 0
        INPUT “please enter a valid positive integer”, price
    ENDWHILE
    reserve_price[item_counter] ← price
NEXT i

FOR i ← 1 TO item _counter
    OUTPUT "item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i]
NEXT i
WHILE loop_constant = 0
    INPUT “Do you want to add more items or bid?  ”, menu_question
    IF menu_question IN [“add”, “Add”, “ADD”]
        INPUT “How many items do you have for auctioning?  ”, item_counter
        FOR i ← 1 TO item_counter
            INPUT “What is the item number of the item you want to add?  ”, number
            WHILE LEN(number) != 3 OR number < 0
                INPUT “please input a valid 3 digit positive integer:  ”, number
            ENDWHILE
            item_numbers[LEN(item_numbers) + item_counter] ← number
            INPUT “What is the description of the item you want to add?  ”, item_des
            WHILE LEN(item_des) < 10
                INPUT “the description has to be at least 10 characters long”, item_des
            ENDWHILE         
            descriptions[LEN(descriptions) + item_counter] ← item_des
            INPUT “What is the lowest price that you are willing to sell this item?  ”, price
            WHILE price < 0
        	    INPUT “please enter a valid positive integer”, price
            ENDWHILE
            reserve_price[LEN(reserve_price) + item_counter] ← price
        NEXT i
        FOR i ← 1 TO LEN(item_numbers)
            OUTPUT "item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i]
        NEXT i
    IF menu_question IN [“bid”, “Bid”, “BID”]
        FOR i ← 1 TO item _counter
        OUTPUT "item number -", item_number[i], ". Description -", description[i], ". Reserve price is", reserve_price[i]
        NEXT i
        INPUT “Which item would you like to look at? (the place in which it is starting from 1 at the tp)”, index_number
        OUTPUT "item number -", item_number[index_number], ". Description -", description[index_number], ". Reserve price is", reserve_price[index_number]
        INPUT “Do you want to bid for this item?”, bid_yesorno
        IF bid_yesorno IN [“yes”, “Yes”, “YES”]
            number_of_bids[index_number] ← number_of_bids[index_number] + 1
            INPUT “What is your bid for this item in dollars?”, bid_amount
        IF bid_amount > 0 
            highest_bid_list[index_number] ← bid_amount
        INPUT “What is your bidder number?”, bidder_number
        highest_bidder_list[index_number] ← bidder_number
    IF menu_question in [“end”, “End”, “END”]
        loop _constant ← 1
