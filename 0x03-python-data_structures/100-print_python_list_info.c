#include <Python.h>

/**
 * print_python_list_info - This function prints python list info
 * @p: is a pyobject
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0, length;
    PyListObject *object;
    PyObject *token;
    const char *token_type

    object (PyListObject *)p;
    length = PyList_Size(p);
    printf("[*] Size of the Python List = %d\n", (int)length);
    printf("[*] Allocated = %d\n", (int)object->allocated)

    while (i < length)
    {
        token = PyList_GetItem(p, i);
        token_type = Py_TYPE(item)->tp_name;
        printf("Element %d: %s\n", i, token_type);
        i++;
    }
    

}