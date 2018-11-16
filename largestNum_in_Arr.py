# Find the largest number in an array

# Defining the largest number function with two arguments array and length
def largest_num(array, length):
   largest = array[0]                  # We assign the largest variable to the first
                                       # number/element in the given array

   for i in range(length):             # use a for loop within the range of length

      if array[i] > largest:           # if the ith element in the array is
                                       # greater than the first element

         largest = array[i]            # Then keep setting the largest value to
                                       # the greatest

   return largest                      # return the largest

# Testing with an unsorted array
array = [5, 20, 7, 0, 9, 20.7, 12, 18]
# Setting the length to the size of the array
length = len(array)

print("Here's the given array: ", array)

print("\nThe Largest number in the array is: ", largest_num(array, length))

# Output:
# Here's the given array:  [5, 20, 7, 0, 9, 20.7, 12, 18]
# 
# The Largest number in the array is:  20.7