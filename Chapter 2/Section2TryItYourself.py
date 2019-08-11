#STRINGS SECTION

# Use a variable to store a name, and print them a message
name = "Jake"
print(f"Hello, {name}! This is a message to you!")

# Use a variable to store a name and print it in lowercase, uppercase, and title case
name = "Jake"
print(f"{name.title()}")
print(f"{name.lower()}")
print(f"{name.upper()}")

#Find a quote from a famous person. Print the quote and the name of its author.
print('The Rebbe once said, "This is the key to time management - to see the value of every moment."')

#Quote, store name in variable, print same thing.
famous_name = "The Rebbe"
print(f'{famous_name} once said, "This is the key to time management - to see the value of every moment."')

#Same thing as above, but add whitespace to name and strip it three ways: lstrip(), rstrip(), and strip().

famous_name = " The Rebbe "

print(f'{famous_name.lstrip()} once said, "This is the key to time management - to see the value of every moment."') # Strips white from left
print(f'{famous_name.rstrip()} once said, "This is the key to time management - to see the value of every moment."') # Strips white from right
print(f'{famous_name.strip()} once said, "This is the key to time management - to see the value of every moment."') # Strips white from left and right

# NUMBERS SECTION

# Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number.
fav_num = 7
print(f"My favorite number is {fav_num}")
print("My favorite number is", fav_num)