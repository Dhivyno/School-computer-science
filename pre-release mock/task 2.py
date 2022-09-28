while True:
 if endday == 1:
   print(paidsum)
   paidsum = 0
   break
 else:
   amountpaid = int(input("What amount have you paid? "))
   while amountpaid < price:
     amountpaid = int(input("You have to pay more than or equal to ", price))
   paidsum += amountpaid
   yesorno = input("Are you done with your parking for today? ")
   if yesorno in ["yes", "Yes", "y", "Y"]:
     endday = 1
