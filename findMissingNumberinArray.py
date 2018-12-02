# Defining the Missing Number Function
def FindMissing(array):
    n = len(array) + 1      # Knowing that there are 5 elements. So, we just add
                            # 1 to whatever the given array length

    given_n = len(array)    # Length of given array

    # Print the number of elements including the missing number
    print("Number of Elements including the missing number in the main array, n =", n)
    # The formula for adding all the elements in an Array including missing number (Arithmetic Progression)
    main_array = n * (n+1) / 2
    # Sum of all elements in the given array
    sum_of_all_elements_in_array = sum(array)
    print("Number of Elements in the given array, n =", given_n)
    print("Sum of all elements in the main array including the missing number =", main_array)
    print("Sum of all elements in the given array =", sum_of_all_elements_in_array)

    # Returning the differece between the main_array and the given array will give us the missing number
    return main_array - sum_of_all_elements_in_array


# Testing with an array
array = [1, 3, 5, 2]
print("Given Array =", array)
result = FindMissing(array)
print("Number", result, "is missing from the array.")

