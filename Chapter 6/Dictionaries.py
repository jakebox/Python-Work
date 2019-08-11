# Dictionaries are a collection of 'key-pair values'.
# Color is key, green is value.
alien_0 = {'color': 'green', 'points': 5}
pnts = alien_0['points']

print(alien_0['color'])
print(f"You have {pnts} points.")

# Adding new key-pair to dictionary. You can also start with an
#                                    empty dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Changing key-value pairs
alien_0['color'] = 'blue'
print(alien_0)

# Deleting key-value pairs
del alien_0['color']
print(alien_0)

# Multi-line dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
print(f"Jen's favorite language is {favorite_languages['jen'].title()}.")

# get() Method
alien_0 = {'color': 'green', 'points': 5}
# The first thing is the key, the second will be the value if the key does not exist.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping through dictionaries
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# items() returns a list of key-value pairs
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping through all the keys

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# For each name in the dictionary favorite_languages, keys only, do this...
for name in favorite_languages.keys():
        print(name.title())

# Cross-checking dictionaries
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah'] # This is a list, not a dictionary

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Looping through values in a dictionary - values() returns 
print("The following languages have been mentioned:")
# For each language in the dictionary favorite_languages, values only, do this...
for language in favorite_languages.values():
    print(language.title())

# Using a "set" - finds unique items
print("The following languages have been mentioned, no repeats:")
for language in set(favorite_languages.values()):
    print(language.title())

# Nesting:

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # List of dictionaries

for alien in aliens:
    print(alien)

# Another one

aliens = [] # List called aliens

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # Add that dictionary to the list

# Modify the first 3 aliens to be different
for alien in aliens[:3]:
    #if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# A list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping.title())

# Dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")