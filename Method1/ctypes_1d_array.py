import ctypes

# Load the shared library
lib = ctypes.CDLL('./libbar.so')

#### Step 3: Passing a 1D Array

#1. **Create a `ctypes` Array**: Convert a Python list to a `ctypes` array.
#2. **Call the C Function**: Pass the array to the function.

# Create a Python list
array_1d = [1, 2, 3, 4, 5]

# Convert to a ctypes array
c_array_1d = (ctypes.c_int * len(array_1d))(*array_1d)

# Define the function signature
lib.modify_1d_array.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int)

# Modify the array in C
lib.modify_1d_array(c_array_1d, len(array_1d), 10)

# Print the modified array in Python
print(list(c_array_1d))  # Outputs: [11, 12, 13, 14, 15]
