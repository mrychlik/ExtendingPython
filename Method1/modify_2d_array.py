from cffi import FFI

ffi = FFI()

# Declare the C function signature
ffi.cdef("""
    void modify_2d_array(int* array, int rows, int cols, int value);
""")

# Load the shared library
lib = ffi.dlopen('./libbar.so')

# Create a 2D array in Python and flatten it to a 1D list
rows, cols = 3, 3
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_array_2d = [item for row in array_2d for item in row]

# Convert to a C array
c_array_2d = ffi.new("int[]", flat_array_2d)

# Call the function to modify the array (e.g., add 10 to each element)
lib.modify_2d_array(c_array_2d, rows, cols, 10)

# Convert the modified array back to a 2D Python list for easy viewing
modified_array_2d = [
    [c_array_2d[i * cols + j] for j in range(cols)]
    for i in range(rows)
]

print(modified_array_2d)
# Outputs:
# [
#     [11, 12, 13],
#     [14, 15, 16],
#     [17, 18, 19]
# ]
