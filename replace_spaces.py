# Keep in Mind: The first solution is a one liner and this will not be considered during the coding interview as it 
# doesn't demonstrate your problem solving skills. I'll post the main solution very soon.

# First Solution:

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

# Second Solution:
