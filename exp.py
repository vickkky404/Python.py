# write a menu driven program to imliment numpy operaion
# 1.create a Numpy array
# 2.perform element wise addition
# 3.find mean , median , standard deviation
# 4. reshape an array
# 5.exit

import numpy as np

def create_array():
    elements = input("Enter elements separated by spaces: ")
    arr = np.array([float(i) for i in elements.split()])
    print("Array created:", arr)
    return arr

def element_wise_addition(arr):
    elements = input("Enter elements for addition (same shape) separated by spaces: ")
    arr2 = np.array([float(i) for i in elements.split()])
    if arr.shape == arr2.shape:
        print("Result of addition:", arr + arr2)
    else:
        print("Arrays must have the same shape!")

def calculate_statistics(arr):
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))

def reshape_array(arr):
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        reshaped = arr.reshape((rows, cols))
        print("Reshaped Array:\n", reshaped)
    except Exception as e:
        print("Error:", e)

arr = None

while True:
    print("\nMenu:")
    print("1. Create a Numpy array")
    print("2. Perform element-wise addition")
    print("3. Find mean, median, standard deviation")
    print("4. Reshape an array")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = create_array()
    elif choice == 2:
        if arr is not None:
            element_wise_addition(arr)
        else:
            print("Create an array first!")
    elif choice == 3:
        if arr is not None:
            calculate_statistics(arr)
        else:
            print("Create an array first!")
    elif choice == 4:
        if arr is not None:
            reshape_array(arr)
        else:
            print("Create an array first!")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
