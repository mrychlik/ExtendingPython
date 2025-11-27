/*----------------------------------------------------------------
* File:     bar.h
*----------------------------------------------------------------
*
* Author:   Marek Rychlik (rychlik@arizona.edu)
* Date:     Wed Nov 26 17:07:51 2025
* Copying:  (C) Marek Rychlik, 2020. All rights reserved.
*
*----------------------------------------------------------------*/
/* The header file is used to declare "exported" functions to
 * other C code. It is used to create the library libbar.so.
 * It is NOT used by Python code CALLING the functions declared
 * In this file: Python must use its own mechanism to inform
 * the 'ctypes' or 'cffi' module about the signatures of
 * the functions (argument types, return type).
 */

#ifndef BAR_H
#define BAR_H

void print_1d_array(int* array, int length);
int bar_add(int x, int y);
void print_2d_array(int* array, int rows, int cols);
void modify_1d_array(int* array, int length);
void modify_2d_array(int* array, int rows, int cols, int value);


#endif	/* BAR_H */
