# Example demonstrating identity operators 'is' and 'is not'

# Define two variables with the same value
x = ["apple", "banana"]
y = ["apple", "banana"]

# Using 'is' to check if they are the same object
print(x is y)  # Output: False, because x and y are different objects in memory

# Using 'is not' to check if they are not the same object
print(x is not y)  # Output: True, because x and y are indeed different objects

# Assign y to x
z = x

# Using 'is' to check if they are the same object now
print(x is z)  # Output: True, because x and z point to the same object in memory

# Using 'is not' to check if they are not the same object
print(x is not z)  # Output: False, because x and z are the same object
