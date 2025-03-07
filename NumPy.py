import numpy as np  # Import NumPy

# Step 1: Create a 1D NumPy Array
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# Step 2: Accessing elements using indexing
print("Element at index 2:", arr[2])  # Accessing the third element

# Step 3: Slicing an array
print("Sliced Array (index 1 to 3):", arr[1:4])

# Step 4: Creating a 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# Step 5: Reshaping an Array
reshaped = arr.reshape((5, 1))  # Reshaping 1D array to 5 rows, 1 column
print("Reshaped Array:\n", reshaped)

# Step 6: Mathematical Operations
arr2 = np.array([5, 4, 3, 2, 1])
sum_arr = arr + arr2  # Element-wise addition
print("Element-wise Addition:", sum_arr)

product_arr = arr * arr2  # Element-wise multiplication
print("Element-wise Multiplication:", product_arr)

sqrt_arr = np.sqrt(arr)  # Square root of each element
print("Square Root of Array:", sqrt_arr)

# Step 7: Random Number Generation
random_matrix = np.random.randint(1, 100, (3, 3))  # 3x3 matrix with random integers
print("Random 3x3 Matrix:\n", random_matrix)

# Step 8: Transposing the 2D Array
transposed = arr_2d.T
print("Transposed 2D Array:\n", transposed)
