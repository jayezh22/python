# Assigning values to variables
a = 10  # assigning 10 to variable a
b = 20  # assigning 20 to variable b
c = 30  # assigning 30 to variable c

# Conditional statement to check which variable is greater
if (a > b) and (a > c):  # checking if a is greater than both b and c
    print("a is greater")  # if true, print "a is greater"
elif b > c:  # if a is not greater, check if b is greater than c
    print("b is greater")  # if true, print "b is greater"
else:  # if both conditions are false, c must be the greatest
    print("c is greater")  # print "c is greater"