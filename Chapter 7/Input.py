# # Taking input
# name = input("Write your name here: ")
# print(f"Hello, {name}!")

# # Multi-line prompt
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello, {name}!")

# # Using int() for numerical input
# age = input("How old are you? ")
# age = int(age) # Converts string input to an integer
# print("You are " + age + " years old.")

# Even or odd using modulo
number = input("Enter a number: ")
number = int(number)

if number % 2 == 0: # Mod (%) returns the remainder of division
    print("This number is even!")
else:
    print("This number is odd!")