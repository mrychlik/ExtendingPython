// foo.c
#include <stdio.h>


int bar_add(int x, int y)
{
  return x+y;
}


void print_1d_array(int* array, int length) {
    for (int i = 0; i < length; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void print_2d_array(int* array, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            printf("%d ", array[i * cols + j]); // Access as a flat array
        }
        printf("\n");
    }
}

// Modify each element of a 1D array by adding 10
void modify_1d_array(int* array, int length) {
    for (int i = 0; i < length; ++i) {
        array[i] += 10;
    }
}

// Modify each element of a 2D array by adding a value
void modify_2d_array(int* array, int rows, int cols, int value) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            array[i * cols + j] += value; // Access as a flat array
        }
    }
}
