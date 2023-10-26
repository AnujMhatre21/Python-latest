# import regex
import re
# . Any Charater except new line character
# ^ Start with 
# $ Ends With
# * Zero or more occurance
# + one or more occurance
# + add multiple condition
# \ search character
# ? ZERO Or one occurance 
# \w search character [@] \W acts reverse
# {} apply condition for particular character, specified number of occurance
# [] A Set number of characters
# \ Escape sequence
# | Either or
# ()  group
#  $ from reverse from back side

# email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# flag = True

# while flag:

#     user_email = input('Enter your Email: ')

#     if re.search(email_condition,user_email):
#         print(user_email +" is a Valid Email")
#         flag = False

#     else: 
#         print("Please enter valid email")


        # Using REgexp 

str = "Anuj Mhatre,Anuj@gmail.com"

matched = re.search("[A-Za-z0-9]{1,50}@[a-z0-9]{1,50}\.[a-z]{2,3}", str)

print(matched)