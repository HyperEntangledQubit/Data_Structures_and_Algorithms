#!/usr/bin/env python3

"""
Example of how to implement a dynamic array in python from scratch.
"""

from ctypes import py_object


class DynamicArray(object):
    """ Implementation of dynamic array data structure in python.

    All arrays are dynamic in python (all of the memory management is handled
    for us in python). This class is meant to explore the concepts of dynamic arrays.

    *Not to be used in production*.

    - **parameters**, **types**, **return** and **return types**::
        :param elements: Number of elements in DynamicArray object.
        :type elements: int, float, string, complex, bool
        :param capacity: Amount of space allocated to store elements.
        :type capacity: integer
    """

    def __init__(self, element = 0, capacity = 1):
        """ Initialize DynamicArray object.
        """
        if not isinstance(element, [int, float, str, complex, bool]):
            raise TypeError(f"Can't instantiate DynamicArray object with {type(element)} type!")
        self.elements = element  # Number of Elements in array.
        self.capacity = int(capacity)  # Amount of Elements array can hold.
        # Create the DynamicArray object.
        self.array = self.make_array(self.capacity)


    def __len__(self):
        """ Retrieve the number of elements in DynamicArray object.

        - **return** and **return types**::
            :return self.elements: Integer number of elements in DynamicArray object.
            :rtype: int
        """
        return self.elements


    def __getitem__(self, index):
        """ Retrieve an element from DynamicArray

        - **parameters**, **types**, **return** and **return types**::
            :param index: Value of index to retrieve the element from within DynamicArray
            :param type: Int
            :return self.array[index]: Element of in DynamicArray at the user defined index.
            :rtype: int, float, string, complex, bool
        """
        # Guard against the user attempting to get an element outside of the array limits.
        if not 0 <= index < self.elements:
            raise IndexError(f"Index {index} is out-of-bounds!")
        return self.array[index]


    def insert(self, element):
        """ Add an element to DynamicArray object.

        - **parameters**, **types**, **return** and **return types**::
            :param element: Element to add to DynamicArray object.
            :type element: int, float, string, complex, bool

        - note::
            In order for DynamicArray object to maintain O(1) the types of all of the elements must be the same.
        """
        # Mimic behavior in static languages by doubling length of array if num of elements and capacity are same.
        if self.elements == self.capacity:
            self._resize(2*self.capacity)
        # Type check to stop user from adding an element to Dynamic array of different type
        newArrType = type(element)
        if self.elements != 0:
            oldArrType = type(self.array[0])  # Get the type of the element in the array currently.
            if newArrType != oldArrType:
                raise TypeError(f"DynamicArray must take the same type for all elements. \
                                You added {newArrType} to a DynamicArray defined with {oldArrType} array")
        self.array[self.elements] = element
        self.elements += 1


    def _resize(self, new_capacity):
        """ Resize DynamicArray object and update capacity.

        - **parameters**, **types**, **return** and **return types**::
            :param new_capacity: Value of size to make new DynamicArray object.
            :param type: Int
        """
        array = self.make_array(new_capacity)  # Allocate memory to use new capacity.
        for element in range(self.elements):
            array[element] = self.array[element]  # Reference all elements in old array and add to newly sized array.
        # Reassign array to new size & assign new capacity.
        self.array = array
        self.capacity = new_capacity


    def make_array(self, new_capacity):
        """ Method used to create DynamicArray objects.

        - **parameters**, **types**, **return** and **return types**::
            :param new_capacity: Value of size to make new DynamicArray objects.
            :param type: Int
            :return Py_object scaled by size: Initialized py_object scaled by size.
            :rtype: Py_Object from ctypes lib.
        """
        if not isinstance(new_capacity, int):
            raise TypeError(f"Parameter {new_capacity} was NOT an integer. DynamicArray size must use int value.")
        return (new_capacity * py_object)()  # py_object is a type multiply by capacity and instantiate it.
