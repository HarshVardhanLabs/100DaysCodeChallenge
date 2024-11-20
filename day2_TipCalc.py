print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $ "))
tip = int(input("How much % of tip would you like to give? 10, 12, or 15? "))
bill_with_tip=(total_bill*(tip/100))+total_bill
print(bill_with_tip)
split_bill=int(input("How many people to split the bill? "))
people_to_pay=bill_with_tip/split_bill
print(f"Each person should pay: ${people_to_pay}")
