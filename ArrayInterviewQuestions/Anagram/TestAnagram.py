#!/usr/bin/env python3


"""
This file tests Anagram solution.
"""

import pytest
from Anagram import Anagram

class TestAnagram():

    """ Test Anagram object.
    """

    @classmethod
    def setup_class(cls):
        cls.anagram = Anagram()
        pass


    @classmethod
    def teardown_clas(cls):
        if cls.anagram is not None:
            del cls.anagram


    # Can the Anagram class be instantiated.
    def test_can_class_be_instantiated(self):
        assert self.anagram is not None, "Class does NOT exist!"


    # Given two strings does Anagram object return a boolean.
    def test_given_two_strings_Anagram_returns_boolean(self):
        # Put in two strings that are anagrams
        assert True == self.anagram("dog", "god")
        # Put in two strings that are NOT anagrams
        assert False == self.anagram("fluffy", "god")


    # Given two strings check that they are anagrams
    def test_Anagram_correctly_checks_if_input_params_are_anagrams(self):
        # Verify that both methods return what is expected
        assert self.anagram._isAnagramFrequency("god", "dog") == self.anagram._isAnagramSorted("dog", "god")  # Anagrams
        assert self.anagram._isAnagramFrequency("god", "fluffy") == self.anagram._isAnagramSorted("dog", "fluffy")  # Not anagrams


    # Verify that frequency method of Anagram object works as expected.
    def test_Anagram_frequency_method_works(self):
        assert True == self.anagram._isAnagramFrequency("Paternal", "Parental")


    # Verify that sorted method of Anagram object works as expected.
    def test_Anagram_sorted_method_works(self):
        assert True == self.anagram._isAnagramSorted("god", "dog")


    # Verify the correct method is called if specified.
    def test_isAnagram_uses_correct_method_to_find_anagram(self):
        assert True == self.anagram.isAnagram("god", "dog", "frequecy")
        assert False == self.anagarm.isAnagram("fluffy", "dog")  # Default is frequency method


    # Verify that generateAnagram method works as expected.
#    def test_generate_Anagram_method_works(self):
#        assert False


if __name__ == "__main__":
    pytest.main()