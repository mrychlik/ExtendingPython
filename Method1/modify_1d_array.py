from cffi import FFI

ffi = FFI()

# Declare the C function signature
ffi.cdef("""
    void modify_1d_array(int* array, int length);
""")

# Load the shared library
lib = ffi.dlopen('./libbar.so')

# Create a 1D Python list and convert it to a C array
array_1d = [1, 2, 3, 4, 5]
c_array_1d = ffi.new("int[]", array_1d)

# Call the function that modifies the array in place
lib.modify_1d_array(c_array_1d, len(array_1d))

# Print the modified array (changes are reflected in Python)
print(list(c_array_1d))  # Outputs: [11, 12, 13, 14, 15]

