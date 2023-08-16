#include <Python.h>

void print_list_info(PyObject* py_list) {
    if (!PyList_Check(py_list)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list object");
        return;
    }

    Py_ssize_t length = PyList_Size(py_list);
    printf("List Length: %ld\n", length);

    for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject* item = PyList_GetItem(py_list, i);
        PyObject* str = PyObject_Str(item);
        const char* c_str = PyUnicode_AsUTF8(str);
        printf("Item %ld: %s\n", i, c_str);
        Py_XDECREF(str);
    }
}

int main() {
    Py_Initialize();

    PyObject* py_list = PyList_New(0);
    PyList_Append(py_list, PyLong_FromLong(42));
    PyList_Append(py_list, PyUnicode_DecodeUTF8("Hello", 5, NULL));
    PyList_Append(py_list, PyFloat_FromDouble(3.14));


    print_list_info(py_list);
    Py_DECREF(py_list);
    Py_Finalize();

    return 0;
}

#include <Python.h>

void print_bytes_info(PyObject* py_bytes) {
    if (!PyBytes_Check(py_bytes)) {
        PyErr_SetString(PyExc_TypeError, "Expected a bytes object");
        return;
    }

    Py_ssize_t length = PyBytes_Size(py_bytes);
    const char* data = PyBytes_AsString(py_bytes);

    printf("Bytes Length: %ld\n", length);
    printf("Bytes Data: %s\n", data);
}

int main() {
    Py_Initialize();
    PyObject* py_bytes = PyBytes_FromStringAndSize("Hello, Bytes!", 12);
    print_bytes_info(py_bytes);
    Py_DECREF(py_bytes);
    Py_Finalize();

    return 0;
}

