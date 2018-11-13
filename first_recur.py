# First Recurring Character in a Given String
# Defining the Function
def recur(str):
   num = {}                            # Creating a Dictionary

   for c in str:                       # A loop to traverse through the given string

      if c in num:                     # If we already find 'c' in the num dictionary,
         return c                      # we'll return it
      else:                            # Else,
         num[c] = 0                    # we'll add the character to num

   print("No Recurring Character!")    # Print if there's no first
                                       # recurring character

# Testing with a string
str = "The Programming Foundation"
# Printing the first recurring character
print("\nThe First Recurring Character is: ", recur(str))

# Output:
# The First Recurring Character is:  r
