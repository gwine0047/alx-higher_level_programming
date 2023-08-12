#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t i = 0;
    PyObject *token;

    list = (PyListObject *)p;
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    while(i < PyList_Size(p))
    {
        token = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(token)->tp_name);
        i++;
    }
}