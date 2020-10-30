#!/usr/bin/env python3

"""
Unit Tests for DynamicArray

TODO - Add doctests to source
"""
import pytest

from DynamicArray import DynamicArray


class TestDynamicArray():

    @classmethod
    def setup_class(cls):
        cls.dynamicArray = DynamicArray()


    @classmethod
    def teardown_class(cls):
        if cls.dynamicArray is not None:
            del cls.dynamicArray


    # Can we instantiate DynamicArray.
    def test_can_DynamicArray_be_instantiated(self):
         assert self.dynamicArray is not None, ValueError


    # Can we insert items into DynamicArray.
    def test_items_can_be_inserted_to_DynamicArray(self):
        # Before the insert
        assert len(self.dynamicArray) == 0
        self.dynamicArray.insert(1)
        # Verify length of DynamicArray changes.
        assert len(self.dynamicArray) == 1


    # Does the capacity of DynamicArray double when elements == capacity.
    def test_capacity_doubles_when_elements_equal_capacity(self):
        # First we need to verify how many items are in DynamicArray
        assert len(self.dynamicArray) == 1
        assert self.dynamicArray.capacity == 1
        # Inserting another element to DynamicArray should cause the capacity to double.
        self.dynamicArray.insert(2)  # O(1)
        assert self.dynamicArray.capacity == 2  # Capacity is doubled here. O(N)
        self.dynamicArray.insert(3)
        assert self.dynamicArray.capacity == 4  # Capacity is doubled here. O(N)
        self.dynamicArray.insert(4)
        assert self.dynamicArray.capacity == 4
        self.dynamicArray.insert(5)
        assert self.dynamicArray.capacity == 8  # Capacity is doubled here. O(N)


    # Are multiple types prevented from being inserted to DynamicArray.
    def test_DynamicArray_can_only_hold_single_type(self):
        # To maintain O(1) insertion time DynamicArray must have a single type because of how they are stored in memory.
        with pytest.raises(TypeError):
            self.dynamicArray.insert("badType")


if __name__ == "__main__":
    pytest.main()
