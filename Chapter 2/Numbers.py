# Adding, subtracting, multiplying, dividing integers
print(2+3)
print(3-2)
print(2*3)
print(3/2)

# Exponents are two asterisks
print(2**10) # 2^10 = 1024

# Order of operations is good too - and parenthesis. Spacing does not matter.
print(2+3*4)
print((2+3)*4)

# Float - any number with a decimal point
print(0.1 + 0.2) # This returns 0.30000000000000004 - we will deal with this later
print(2 * 0.1)

print(4/2) # This is a float - whenever you divide two integers a float is returned. Int/Int = float.
print(2 * 3.0) # Mixing ints and floats gives you floats.

# Underscores can be used to space numbers, if wanted. (only python3.6>)
fat_number = 14_000_000_000
print(fat_number) # The _ go away

# Assigning multiple variables and values at the same time
x, y, z = 0, 0, 0