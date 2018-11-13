# Keep in Mind: The first solution is a one liner and this will not be considered during the coding interview as it 
# doesn't demonstrate your problem solving skills.

# First Solution:

# Defining the "Replace spaces" Function
def replace_spaces(str):
   return "%20".join(str.split())      # One line solution using the join and str
                                       # functions in Python

# Testing with a string
str = "Hello, I am bootkernel!"
print("Given String:", str)             # Prints given string
print("\nHere's the given string with the spaces replaced:", replace_spaces(str))

# Output:
# Given String: Hello, I am bootkernel!
#
# Here's the given string with the spaces replaced: Hello,%20I%20am%20bootkernel!

# Second Credible Solution:
# Defining the credible "Replace spaces" Function
def replace_spaces_credible(str):
   replace = ''                              # Blank variable that holds nothing
   for c in str:                             # A loop to traverse through the
                                             # given string

      if (c == ' '):                         # if c/char is 'white_space',
         replace = replace + '%20'           # replace the whitespace with %20

      else:                                  # Else,
         replace = replace + c               # replace the whitespace with c
   return replace

# Testing with a string
str = "Hello, I am bootkernel!"

print("Given String:", str)                  # Prints given string

print("\nHere's the given string with the spaces replaced:", replace_spaces_credible(str))

# Output:
# Given String: Hello, I am bootkernel!
#
# Here's the given string with the spaces replaced: Hello,%20I%20am%20bootkernel!
