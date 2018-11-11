#Assigning Numbers
x = 1
y = 0

print("Original Values (x, y):", x, y)

#Using XOR to swap values instead of using a temporary variable
x ^= y
y ^= x
x ^= y

print("Swapped Values (x, y):", x, y)

# Output:
# Original Values (x, y): 1 0
# Swapped Values (x, y): 0 1

