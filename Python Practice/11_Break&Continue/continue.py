# Initialize a variable i to 0
i = 0

# Use a while loop to iterate as long as i is less than 6
while i < 6:
    # Check if i is equal to 3
    if i == 3:
        # If i is 3, increment i by 1 (so it becomes 4)
        i += 1
        # Use the continue statement to skip the rest of the current iteration
        # and move on to the next iteration
        continue
    # Print the current value of i (but not when i is 3, because of the continue statement)
    print(i)
    # Increment i by 1
    i += 1