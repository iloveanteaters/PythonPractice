# In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.
# Lets assume we have a list of letters:
# letters = ["a", "b", "c", "d", "e", "f", "g"]
# Suppose we want to select from "b" through "f".

#We can do this using the following syntax: letters[start:end], where:

# start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
# end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Modify beginning, so that it selects the first 2 elements of suitcase.
beginning = suitcase[0:2]
print(beginning)
# print pants pants
middle = suitcase[2:4]
print(middle)


# If we want to select the first n elements of a list, we could use the following code:fruits[:n]
# The following code would start slicing from index 0 and up to index 3. print(fruits[:3])

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Create a new list called last_two_elements containing the final two elements of suitcase.
last_two_elements = suitcase[-2:]
print(last_two_elements)

# Create a new list called slice_off_last_three containing all but the last three elements.
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# In Python, it is common to want to count occurrences of an item in a list.
# If we want to know how many times i appears in this word, we can use the list method called .count():

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Getting the amount of jake votes
jake_votes = votes.count("Jake")
print(jake_votes)

# Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.
# We can sort a list using the method .sort().

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
# sorting addresses
addresses.sort()
print(addresses)

# Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

# Use print to examine sorted_cities. Why is it not the sorted version of cities?
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

# Editing sort to make it reverse order^
