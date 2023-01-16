num_char= len(input("What is your name?"))
# print("Your name has " + num_char +"characters")

# type() = function to see what the data type is

# print(type(num_char))

# But with this you would have gotten a type error , because you can only concatenate strings , not int.

# str() , int() , float() = to convert the piece of data you want

new_num_char= str(num_char)

print("Your name has" + " " +new_num_char + " " + "characters")

# In this case we've taken a integer data type , put it inside the parentheses of a str function which takes a object in between the parentheses and converts it into a string





