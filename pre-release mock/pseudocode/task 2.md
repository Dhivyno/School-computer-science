 REPEAT
   INPUT "What amount have you paid?", int, amountpaid
   WHILE amountpaid < price DO
     INPUT "You have to pay more than or equal to the price", int, amountpaid
   ENDWHILE
   paidsum ← paidsum + amountpaid
   INPUT "Are you done with your parking for today?”, str, yesorno
   IF yesorno IN ["yes", "Yes", "y", "Y"]:
     endday ← 1
UNTIL endday = 1 
OUTPUT paidsum
paidsum ← 0
