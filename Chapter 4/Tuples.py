# Tuples are like lists that won't change - "immutable"

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# We can loop through tuples normally.
for dimension in dimensions:
    print(dimension)

# While tuples cannot be changed, you can overwrite the entire variable

dimensions = (500, 20)
print(dimensions)