print("Welcome to the tip calculator!")
bill= float(input("What was the total bill?"))
percent= int(input("What percentage tip would you like to give?10 , 12 or 15?"))
person=int(input("How many people to split the bill?"))

tip_percent = percent / 100 
total_tip= bill * tip_percent
total_bill= bill + total_tip
bill_person = total_bill / person 
total_round = round(bill_person,2)

print(f"Each person should pay:{total_round}")

