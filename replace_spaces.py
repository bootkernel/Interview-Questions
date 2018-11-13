# Defining the "Replace spaces" Function
def replace_spaces(str):
   return "%20".join(str.split())      # One line solution using the join
                                       # function in Python

# Testing with a string
str = "Hello, I am bootkernel!"
print("Given String:", str)             # Prints given string
print("\nHere's the given string with the spaces replaced:", replace_spaces(
   str))

# Output:
# Given String: Hello, I am bootkernel!
#
# Here's the given string with the spaces replaced: Hello,%20I%20am%20bootkernel!