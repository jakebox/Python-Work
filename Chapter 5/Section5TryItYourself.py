# Chapter 5 Try it yourself

# Stages of Life
# age = 20

# if age < 2
#     print("Baby")
# elif age >= 2 and <4
#     print("Toddler")
# elif age > 4 and <13
#     print("Kid")
# elif age > 13 and <20
#     print("Teenager")
# elif age > 20 and <65
#     print("Adult")
# else:
#     print("Elder")

# Dictionaries

# Rivers
rivers = {'nile': 'egypt', 'mississippi': 'the united states', 'yellow river': 'china' }
for river, country in rivers.items():
    print(f"The {river.title()} is in {country.title()}.")
print("Rivers:")
for river in rivers.keys():
    print(f"\t{river}")
print("Countries:")
for country in rivers.values():
    print(f"\t{country}")

print("\n")
# Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
should_take = ['jen', 'steve', 'sarah', 'mark']

for people in should_take:
    if people in favorite_languages.keys():
        print(f"{people.title()}, you took the poll!")
    else:
        print(f"{people.title()}, you need to take the poll.")

print("\n")
# Cities

cities = {
    'chicago': {
        'population': 2_700_000,
        'state': 'illinois',
        'nickname': 'the windy city',
    },

    'st. louis': {
        'population': 319_000,
        'state': 'missouri',
        'nickname': 'st. louie'
    },

    'new york': {
        'population': 8_000_000,
        'state': 'new york',
        'nickname': 'the big apple',
    },
}

for city, city_info in cities.items():
    print("\n" + city.title())
    print(f"\tPopulation:", city_info['population'])
    print(f"\tState:", city_info['state'].title())
    print(f"\tNickname:", city_info['nickname'].title())