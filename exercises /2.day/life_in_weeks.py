age = input("What is your current age? ")

int_age = int(age)

life = 90 - int_age 

days = life * 365
weeks = life * 52
months = life * 12

print(f"You have {days} days, {weeks} weeks and {months} months left")