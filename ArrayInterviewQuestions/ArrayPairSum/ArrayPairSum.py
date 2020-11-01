#!/usr/bin/env python3

"""
Given an array output all the unique pairs that sum up to a specific value k.

This one feels weird to make an entire class for. So I'll make it w/ just a few methods.
Note - This is only because this is so small. You shouldn't do this in production. We want to
keep our source code separate from our test code.
"""
import pytest


def generatePairSum(search_array, expected_value):
    """ Returns all of the pairs whose elements sum up to expected_value
    """
    if len(search_array) < 2:
        raise ValueError("Must enter a search_array with at least 2 elements to create ordered pairs")
    return [(x,y) for x in search_array for y in search_array[::-1] if x+y == expected_value]


# Does generatePairSum raise a ValueError when a search_array that is too small is entered?
def test_generatePairSum_raises_exception_when_search_array_is_too_small():
    with pytest.raises(ValueError):
        generatePairSum([1], 1)


# Does generatePairSum return the correct amount of pairs?
def test_generatePairSum_returns_correct_amount_of_pairs():
    assert len(generatePairSum([1,2,3,4,5], 3)) == 2
    assert len(generatePairSum([1,2,3,4,5], 7)) == 4


# Does generatePairSum return the correct pairs?
def test_generatePairSum_returns_correct_pairs():
    assert generatePairSum([1,2,3,4,5], 3) == [(1, 2), (2, 1)]
    assert generatePairSum([1,2,3,4,5], 7) == [(2, 5), (3, 4), (4, 3), (5, 2)]


if __name__ == "__main__":
    pytest.main()