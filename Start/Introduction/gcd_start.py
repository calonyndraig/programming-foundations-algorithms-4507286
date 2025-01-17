# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while b != 0: # while b is not zero
        temp = a # sets current a to a temp variable
        a = b # sets a to b (since b will be the next a we try or the remainder)
        b = temp % b # sets the remainder to b
    return a

# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
print(gcd(120,25)) # should be 5
