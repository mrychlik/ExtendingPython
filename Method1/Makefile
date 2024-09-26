CFLAGS=-std=c99
PYTHON=python

all: libbar.so

libbar.so: bar.c
	gcc -shared -I/usr/include/python3.12 -o $@ -fPIC bar.c

check: add_check pass_array_check modify_array_check \
	ctypes_1d_arrays_check ctypes_2d_arrays_check

add_check: bar_ext.py  libbar.so
	$(PYTHON) ./bar_ext.py

pass_array_check: pass_arrays.py libbar.so
	$(PYTHON) ./pass_arrays.py

modify_array_check: modify_array_1d_check modify_array_2d_check

modify_array_1d_check: modify_1d_array.py libbar.so
	$(PYTHON) modify_1d_array.py

modify_array_2d_check: modify_1d_array.py libbar.so
	$(PYTHON) modify_2d_array.py

ctypes_1d_arrays_check: ctypes_1d_array.py libbar.so
	$(PYTHON) ctypes_1d_array.py

ctypes_2d_arrays_check: ctypes_2d_array.py libbar.so
	$(PYTHON) ctypes_2d_array.py


clean: FORCE
	-rm *.so

FORCE:
