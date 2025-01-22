# Example file for Programming Foundations: Algorithms by Joe Marini
# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = {}

# TODO: iterate over each item and increment the count for each one

for item in items:
  if item in counter:
    counter[item] += 1
  else:
    counter[item] = 1

# print the results
print(counter)
