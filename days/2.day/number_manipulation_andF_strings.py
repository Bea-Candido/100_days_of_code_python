print(int(8/3))

# How to round numbers?

print(round(8/3))

# You can specify the number of digits of precision you want to round it to

print(round(8/3,2))

# Because we know that whenever we divide any number by any other number, the result always gets turned into a floating point number.
# So, if you din't want that and you just wanted an integer , you can just use the floor division like this

print( 8 // 3)

# / float 
# // int

# +++ Manipulate a value

# score=0

# Say for example if you're keeping track of the user's score , so you could have score = 0 to begin with and every single time in your code say a user scores a point 

#User scores a point 

# score = score + 1
# # is the same:
# score += 1

# So this is really handy when you have to manipulate a value based on its previous value, which you'' ll have to d a lot in programming  

#  +++ For mix strings and different data types:
# f-String

score= 0
height = 1.8
isWinning = True

print(f"You score is {score}")
print(f"You height is {height}")
print(f"You are winning {isWinning}")





