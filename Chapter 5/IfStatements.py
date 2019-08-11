# Simple IF statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars: # For each car in the list cars
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Not Equal
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # != means NOT
    print('Hold the anchovies!')

# Mathematical comparisions are good too:
# < <= > >=
# You can also check multiple things:
# age0 >= 21 and age0 <=50
# age0 >= 21 or age0 = 10

# Checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
# ^ Will return True

# Checking if a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users: # If the user is not in list banned_users
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean expressions
game_active = True
can_edit = False

# If-else
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you cannot vote.")


# if-elif-else / multiple elif (else if)
age = 3.5
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
elif age < 65:
    print("Your admission cost is $40")
else:
    print("Your admission cost is $20")

# If statements with lists