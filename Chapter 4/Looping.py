magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)
print('\n')
for magician in magicians:
    print(f"{magician.title()} that was a great trick!")
print ("\nThe end!")

# Range function
for value in range(1, 6):
    print(value)

# Making lists of numbers with range()
numbers = list(range(1, 6))
print(numbers)

# Skipping numbers in range()
even_numbers = list(range(2, 11, 2)) # Starts with 2, goes until 11, adding 2 each time
print(even_numbers)

# Printing first 10 square numbers
squares = []
for value in range(1, 11):
    squares.append(value**2) # square is the iteration to the second power (1^2, 2^2, 3^2...) / adds that to the list
print(squares) # prints the list

# Finding mins, maxs, sums
digits = [value+1 for value in range(0,100)] # Make list name. Open brack
print(min(digits))
print(max(digits))
print(sum(digits))
print(digits)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # Prints first 3 indexes
print(players[2:]) # prints from second index (third thing) to the end
print(players[-3:]) # Prints last three indexes

# Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("These are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Make a slice with no first or second index and it will include the whole list
# You can't just do: friend_foods = my_foods, as this will point friend_foods to the same list, and not make a copy
# Copy lists using a slice! [:]
print(my_foods)
print(friend_foods)

my_foods.append('Oranges')
friend_foods.append('Apples')

print(my_foods)
print(friend_foods) 