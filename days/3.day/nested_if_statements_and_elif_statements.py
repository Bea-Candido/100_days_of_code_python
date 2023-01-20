# +++ Nested if/else statement :
# In a nested if statement, once the first condition has passed we can check for another condition.
# And then we can have another if/else statement. 
#  ex:
# if condition:
#   if another condition:
#     do this
#   else:
#     do this
# else:      
#   do this 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("What is your age?"))
   if age < 12:
      print("Please pay $5")
   elif age <= 18:
      print("Please py $7")
   else:
      print("Please pay $12")   
else:
   print("Sorry, you have to grow taller before you can ride")  




# +++ if /elif /else 

# We could use something called the elif. Instead of having a simple if/else statement you can add as many elif conditions as you want. So we can check for condition

