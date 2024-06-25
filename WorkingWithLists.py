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
