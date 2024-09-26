from cffi import FFI

ffi = FFI()

# Declare the C function signatures
ffi.cdef("""
    void print_1d_array(int* array, int length);
    void print_2d_array(int* array, int rows, int cols);
""")

# Load the shared library
lib = ffi.dlopen('./libbar.so')

# Pass a 1D array
array_1d = [1, 2, 3, 4, 5]
c_array_1d = ffi.new("int[]", array_1d)
lib.print_1d_array(c_array_1d, len(array_1d))

# Pass a 2D array (flattened)
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_array_2d = [item for row in array_2d for item in row]
c_array_2d = ffi.new("int[]", flat_array_2d)
lib.print_2d_array(c_array_2d, len(array_2d), len(array_2d[0]))

# Pass a 2D array using allocated memory
rows, cols = 3, 3
c_array_2d = ffi.new(f"int[{rows}][{cols}]")
for i in range(rows):
    for j in range(cols):
        c_array_2d[i][j] = i * cols + j + 1

lib.print_2d_array(ffi.cast("int*", c_array_2d), rows, cols)
