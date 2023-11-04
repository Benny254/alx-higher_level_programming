/*
 * File: 100-print_python_list_info.c
 * Auth: Benard Odhiambo
 */

#include <Python.h>

/**
 * print_python_list_info - to print basic info about Python lists.
 * @p: The PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, j;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	int j = 0;
	while (j < size) 
	{
	printf("Element %d: ", j);

	obj = PyList_GetItem(p, j);
	printf("%s\n", Py_TYPE(obj)->tp_name);

	j++;
	}
}
