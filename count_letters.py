# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/17/2022
# Description: Takes a string and returns a dictionary that shows how many of each letter is in the string.

def count_letters(string):
    """Counts the number of each letter in a string."""

    letter_count = {}

    for character in string:

        upper_char = character.upper()

        if "A" <= upper_char <= "Z":

            if upper_char in letter_count:

                letter_count[upper_char] += 1

            else:

                letter_count[upper_char] = 1

    return letter_count