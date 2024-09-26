// foo.c
#include <Python.h>

// A simple function to be called from Python
static PyObject* foo_add(PyObject* self, PyObject* args) {
    int a, b;
    // Parse Python arguments
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    // Return result as a Python object
    return Py_BuildValue("i", a + b);
}

// Method definition
static PyMethodDef FooMethods[] = {
    {"add", foo_add, METH_VARARGS, "Add two numbers."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition
static struct PyModuleDef foo_module = {
    PyModuleDef_HEAD_INIT,
    "foo", // name of the module
    NULL,  // module documentation
    -1,    // state keeping
    FooMethods
};

// Initialization function (must be called PyInit_<modulename>)
PyMODINIT_FUNC PyInit_foo(void) {
    return PyModule_Create(&foo_module);
}
