# To kick us off we create a function that will add one to a number whenever it is called. We'll then assign the function to a variable and use this variable to call the function.
def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)

# Next, we'll illustrate how you can define a function inside another function in Python. Stay with me, we'll soon find out how all this is relevant in creating and understanding decorators in Python.

def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)

# This code defines a function called plus_one that takes in a parameter called number.
#• Within the plus_one function, there is another function called add_one that takes in a parameter also called number and returns the value of number + 1.
#• The plus_one function then calls the add_one function with the number parameter passed in, and assigns the result to a variable called result.
#• Finally, the plus_one function returns the value of result.
#• When the code is executed, the plus_one function is called with the argument 4.
#• This causes the add_one function to be called with the argument 4, which returns the value 5.
#• The plus_one function then returns the value of result, which is 5.

#Functions can also be passed as parameters to other functions. Let's illustrate that below.
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

# Functions can also be passed as parameters to other functions. Let's illustrate that below.
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

#A function can also generate another function. We'll show that below using an example.
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

#Python allows a nested function to access the outer scope of the enclosing function. This is a critical concept in decorators -- this pattern is known as a Closure.
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")
