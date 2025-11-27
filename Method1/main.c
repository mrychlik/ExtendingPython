/*----------------------------------------------------------------
* File:     main.c
*----------------------------------------------------------------
*
* Author:   Marek Rychlik (rychlik@arizona.edu)
* Date:     Wed Nov 26 10:41:34 2025
* Copying:  (C) Marek Rychlik, 2020. All rights reserved.
*
*----------------------------------------------------------------*/
// This is a pure C driver for the library libbar.so

#include "bar.h"

void test_print_1d_array()
{
  int array[] = {1,2,3};
  print_1d_array(array, sizeof(array)/sizeof(*array));
}





int main(int argc, char *argv[])
{
  test_print_1d_array();


}
