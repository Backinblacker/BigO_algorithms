# Task Number 1
# Given a numeric value, determine if it is even or odd
# The function should take in the value as a parameter and return a boolean value (T if even, F if odd)
# Comment stating the time complexity
# Take a screenshot and upload it to the personal instructor slack channel

# O(log n) time complexity
def is_even(number):
    if number %2 == 0:
        return True
    else:
        return False

even_number = is_even(8)
odd_number = is_even(11)

print(even_number)
print(odd_number)

# Task Number 2
# Given a list of numbers, determine if each item in the list is lower than 100
# The function should take in the list as a parameter and retunr a boolean value 
# (False if there are any numbers greater than equal to 100, True if all numbers are less than 100.)
# Comment stating the time complexity
# Take a screenshot and upload it to the personal instructor slack channel

def less_than_100(list_of_numbers):
    pass

# Task Number 3
# Given a list of names, determine if any names are contained in the list more than once
# The function should take in the list as a parameter and return a boolean value
# True if there are repeated names, False if there are no repeats
# Comment time complexity
# Take a screenshot and upload it to the personal instructor slack channel

def duplicate_names(names_list):
    pass

# Task Number 4
# Given a list of numbers, MANUALLY sort the list into ascending order
    # Suggested Strategy
        # Starting with the first two numbers, compare them to see which is larger
        # Place the lower number to the left and the higher number to the right
        # Iterate through the list, checking each pari of numbers one at a time
        # Repeat from the start until the list is sorted
# Comment time complexity
# Take a screenshot and upload it to the personal instructor slack channel

def sort_list (arr):
    pass

unsorted = [10, 120, 15, 3, 65, 49, 17, 100, 13]
sorted = sort_list(unsorted)