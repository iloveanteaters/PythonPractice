class Dog:
  # To create a Dog, give it a name, breed, and age. age is in years. 
  # If you don't give an age, we'll say it's 0 years old (a puppy).
  # All dogs also start as friendly!
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
    # self.name is this specific dog's name
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
