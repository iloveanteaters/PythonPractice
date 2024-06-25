# Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo that can cause an error.

#Python gives us an easy way of creating these types of lists using a built-in function called range().

#The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.

#So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

# that it is a range containing numbers starting at 0 and up to, but not including, 9.

number_list = range(9)
print(list(number_list))

#Create a range called zero_to_seven with the numbers 0 through 7.
zero_to_seven = range(8)
print(list(zero_to_seven))

# By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.
# For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

# Example : Starts at 5
# Has a difference of 3 between each item
# Ends before 15

range_five_three = range(5, 15, 3)


# Create a range called range_diff_five that:
# Starts at 0
# Has a difference of 5 between each item
# Ends before 40

range_diff_five = range(0, 40, 5)

# Often, we’ll need to find the number of items in a list, usually called its length.
# We can do this using a built-in function called len().
# When we apply len() to a list, we get the number of elements in that list:

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

# Calculate the length of long_list and save it to the variable long_list_len.

long_list_len = len(long_list)
print(long_list_len)

# Calculate its length using the function len() and save it to a variable called big_range_length.
big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length)
