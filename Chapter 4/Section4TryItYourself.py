# Try it yourself Chapter 4

# For loop, print numbers 1-20

for i in range (1, 21):
    print(i)


numbers = list(range(1, 1000001))
print(sum(numbers))

# List of odd numbers from 1 to 20. Use for loop.
odd_nums = list(range(1, 21, 2))
for num in odd_nums: # "for every number in odd_num, print the number"
    print(num)

# List of multiples of 3 from 3 to 30. Use a for loop to print the numbers in the list.
mult_of_three = list(range(3, 31, 3))
for num in mult_of_three:
    print(num)

# Make a list of the first 10 cubes and print using for loop.
cubes = [value**3 for value in range(2,11)]
print(cubes)

# Tuples - buffet challenge

menu = ('pizza', 'chicken', 'pasta', 'water', 'hamburger')
for item in menu:
    print(item.title(print(my_foods)
print(friend_foods)))
# menu[0] = 'ham' -- Will throw an error b/c tuples can't be changed
menu = ('pizza', 'ham', 'pasta', 'tea', 'hamburger') # Writing over the variable
print("\nNew Menu:")
for item in menu:
    print(item.title())