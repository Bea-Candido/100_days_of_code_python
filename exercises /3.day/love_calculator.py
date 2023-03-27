print("Welcome to the love calculator")
name1= input("What is your name?\n")
name2 = input("What is your name?\n")

combination_of_names = name1 + name2
names_lower = combination_of_names.lower()
t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
total_1 = t + r + u + e

l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")
e = names_lower.count("e")
total_2 = l+o+v+e 

love_score = int(str(total_1)+ str(total_2))

if (love_score < 10) or (love_score < 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.") 
else:
  print(f"Your score is {love_score}")   