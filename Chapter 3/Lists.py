# Lists are denoted by sqaure brackets
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # This prints everything, in the formatting above

print(bicycles[0]) # This prints the first thing in the list
print(bicycles[0].title()) # We can also use methods here
print(bicycles[-1]) # -1 automatically points to the last item in a list

# Using individual values from a list in a message

print(f"My first bicycle was a {bicycles[0].title()}.")

# TRY IT YOURSELF

# Names. Store a few of your friends in a list called names. Print one at a time.
names = ['Finn', 'Ryder', 'Lucas', 'Jacobe']
print(names[0])
print(names[1])

# Same as above, but print a message to them.
names = ['Finn', 'Ryder', 'Lucas', 'Jacobe']
print(f"Hello, {names[0]}")

# Modifying list items
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # Adds this to the end of the list
print(motorcycles)

# Inserting element into a specific part of the list\
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Deleting items from a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[0]
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

# 'Popping' item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(-1) # Popping off last item from the list
print(motorcycles)
print(popped_motorcycle)

# Sorting a list

cars = ['bmw', 'audi', 'toyota', 'acura']
cars.sort() # Sorts list alphabetically
print(cars)
cars.sort(reverse=True) # Sorts list reverse alphabetically
print(cars)

# Just printing a list sorted
print(sorted(cars))

# Length of list
print(len(cars)) # 4


# LISTS PRACTICE PROBLEMS

places = ['Japan', 'Mt Ranier', 'Yellowstone', 'Yosemite', 'North Korea']

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
print("There are", len(places), "places that I want to go to.")
print(f"There are {len(places)} places that I want to go to.")