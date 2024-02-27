print("Welcome to the tip calculator!")
Total_bill=float(input("what was the total bill $"))
No_people=int(input("Enter the n.o of people"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
# calculation
bill_with_tip=(Total_bill/100)*tip+Total_bill
bill_split=round(bill_with_tip/No_people,2)
print(bill_split)