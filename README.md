Building a Python Extension
==================================
In this folder you also have examples of turning C code into Python commands.
Two ways are covered:

Method1: Calling functions directly via cffi (C Foreign Function Interface).
-------------------------------------------------------------------
C functions are build directly into a 
* DLL (.dll) on Windows or 
* Shared Objects (.so) files under Linux..

The file bar_ext.py is an example of this approach. It calls functions in the
library libbar.so (Linux).

Two approaches are tested:
* Based on 'ctypes' package
* Based on 'cffi' package


Method2: Building a full Python Package
------------------------
The consequential file is setyp.py. To build the extension you run:

	python setup.py build
	
To install the extension you do:

	python setup.py install

Disclaimer
=========
This code is very minimalistic and it is designed purely for illustration and educational purposes. The author is takes no responsibility resulting from its use.
