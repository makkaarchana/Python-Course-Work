print("------Identity Operators------")

# Creating two different lists with same elements
a = [10, 20, 30]
b = [10, 20, 30]

# Comparing two lists
print("a == b:", a == b)
print("a is b:", a is b)
print("a is not b:", a is not b)

# Displaying object IDs
print("ID of a:", id(a))
print("ID of b:", id(b))

# Assigning one list to another variable
c = a

# Comparing a and c
print("a == c:", a == c)
print("a is c:", a is c)
print("a is not c:", a is not c)

# Displaying object IDs
print("ID of a:", id(a))
print("ID of c:", id(c))