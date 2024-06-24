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
