# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("Hello")
    print("Hello")


greet()


# function that allows for input
def greet_with_name(name):  # parameter
    print(f"Hello {name}")


greet_with_name("rui")  # argument


# functions with more than one 1 input - position arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("rui", "lisbon")

# call function with keyword arguments - order of arguments does not matter
greet_with(location="porto", name="pedro")
greet_with(name="ana", location="faro")
