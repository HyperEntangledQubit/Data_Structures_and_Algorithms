#!/usr/bin/env python3

"""
Given two strings, check to see if they are anagrams. Ignore spaces and capitalization.

Anagram is when two strings can be written with the exact same letters.
"""
from string import ascii_lowercase

class Anagram():

    """ Object used to check if a given string is an Anagram.

        TODO - Optimize this class. We don't need two ascii character arrays.
        TODO - Perform Big-O analysis
    """


    def __init__(self, string1 = None, string2 = None):
        """ Initialize input params
        """
        self.first  = string1
        self.second = string2


    def __call__(self, string1, string2):
        """ Makes Anagram object callable
        """
        return self.isAnagram(string1, string2)


    def isAnagram(self, string1, string2, method = "sorted"):
        """ Checks that input params are anagrams of each other.

            Two methods:
                1. If both strings have the same frequency of letters -- True
                2. If both strings are equal to each other once sorted -- True
        """
        # Base case number of letters in each string must be the same.
        if len(string1) != len(string2):
            return False  # Strings passed in are NOT anagrams.

        if method == "sorted":
            return self._isAnagramSorted(string1, string2)
        else:
            return self._isAnagramFrequency(string1, string2)


    def _isAnagramFrequency(self, string1, string2):
        """ Method 1 check that both strings have the same frequency of letters
        """
        # Parse each string into its own dictionary of lowercase acii letters.
        string1_occurances_dict = self._buildOccuranceDict(string1)
        string2_occurances_dict = self._buildOccuranceDict(string2)
        # Compare the two strings and return a boolean.
        return string1_occurances_dict == string2_occurances_dict


    def _buildOccuranceDict(self, string):
        """ Returns a dictionary of lowercase acii occurances from input string.
        """
        # Create a dictionary of all lowercase acii letters.
        string_occurance_dict = self._buildASCIIDict()
        ascii_occurance_dict = self._buildASCIIDict()

        # Parse string into its own dictionary of occurances.
        for key in ascii_occurance_dict:
            for letter in string.lower():
                if key == letter:
                    string_occurance_dict[key] += 1
        return string_occurance_dict


    def _buildASCIIDict(self):
        """ Helper to build lowercase ascii dict
        """
        ascii_occurance_dict = {}
        for i,j in enumerate(ascii_lowercase):
            ascii_occurance_dict[j] = 0
        return ascii_occurance_dict


    @staticmethod
    def _isAnagramSorted(string1, string2):
        """ Method 2 check that both strings are equal to each other once sorted.
        """
        # Remove spaces and lower case each input string.
        string1 = string1.replace(" ", "").lower()
        string2 = string2.replace(" ", "").lower()

        return sorted(string1) == sorted(string2)


    @staticmethod
    def generateAnagram(string):
        """ Pass in a string and generate anagrams.

        TODO - Fill this method out as a part of Issue number 13
        """
        pass