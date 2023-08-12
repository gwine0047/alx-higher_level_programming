#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - This function prints python list info
 * @p: is a pyobject
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, length;
	PyListObject *object;

	length = PyList_Size(p);
	object = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", object->allocated)
	for (i = 0; i < length; i++)
		printf("Element %li: %s\n", i, Py_TYPE(object->ob_item[i]->tp_name))
}