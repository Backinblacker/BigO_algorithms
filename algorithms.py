# Task Number 1
# Given a numeric value, determine if it is even or odd
# The function should take in the value as a parameter and return a boolean value (T if even, F if odd)
# Comment stating the time complexity
# Take a screenshot and upload it to the personal instructor slack channel

# O(1) time complexity
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

#O(n^2) time complexity
def less_than_100(list_of_numbers):
    for number in list_of_numbers:
        if number > 99:
            print("False")
            return False
    print("True")
    return True
        
less_than_100 ([1, 50, 6 , 50, 25, 250])
less_than_100 ([1, 3, 10, 99, 55])

# Task Number 3
# Given a list of names, determine if any names are contained in the list more than once
# The function should take in the list as a parameter and return a boolean value
# True if there are repeated names, False if there are no repeats
# Comment time complexity
# Take a screenshot and upload it to the personal instructor slack channel

# def duplicate_names(names_list):
#     duplicate_found = False
#     while True:
#         for name in names_list:
#             if names_list == name:
#                 return True
#         if duplicate_found == False:
#             return False

# list_of_names = ["JJ", "Megan", "Gavin", "Chris", "Chris", "Kyle", "Slagathor"]
# duplicate_question = duplicate_names(list_of_names)

# Task Number 4
# Given a list of numbers, MANUALLY sort the list into ascending order
    # Suggested Strategy
        # Starting with the first two numbers, compare them to see which is larger
        # Place the lower number to the left and the higher number to the right
        # Iterate through the list, checking each pari of numbers one at a time
        # Repeat from the start until the list is sorted
# Comment time complexity
# Take a screenshot and upload it to the personal instructor slack channel

# O(n^3) time complexity
def sort_list (numbers):
    length = len(numbers) - 1
    unsorted = True

    while unsorted:
        unsorted = False
        for number in range(0,length):
            if numbers[number] > numbers[number + 1]:
                hold = numbers[number + 1]
                numbers[number + 1] = numbers[number]
                numbers[number] = hold
                unsorted = True
    print(numbers)

unsorted = [10, 120, 15, 3, 65, 49, 17, 100, 13]
sorted = sort_list(unsorted)