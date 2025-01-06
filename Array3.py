# Array using array module

# using array() instead of list array because it is memory efficient,The list consumes more memory compared to array()..


import array

# declaring the array
my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array)

# Common Type Codes:
# 'i': Signed integer (2 bytes)
# 'f': Floating point number
# 'd': Double precision floating point number
# 'u': Unicode character
# 'b': Signed byte
# 'B': Unsigned byte


# prints the length of the array..
print(len(my_array))
