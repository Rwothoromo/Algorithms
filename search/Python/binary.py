"""
Binary Search (uses Divide and Conquer) takes in a list of sorted elements and the value to be found.
The first step is to compare the provided value with the element in the middle of the list.
If there is a match, the search comes to an end, otherwise, work with one half of the list.
The selected half is more comparable to the sought value than the other.
Implemented recursively.
"""


def binary_search(sorted_list, sought_value):
    """Return the index of the sought value in the sorted list"""

    first_index = 0
    last_index = len(sorted_list) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        mid_value = sorted_list[mid_index]

        # match found!
        if mid_value == sought_value:
            return mid_index

        # work with right half
        if sought_value > mid_value:
            first_index = mid_index + 1
        else:
            # work with left half
            last_index = mid_index - 1

    # no match
    if first_index > last_index:
        return None


def binary_search_recursive(sorted_list, first_index, last_index, sought_value):
    """Return the index of the sought value in the sorted list, given first & last indices"""

    # no match
    if first_index > last_index:
        return None

    else:
        mid_index = first_index + ((last_index - first_index) // 2)
        mid_value = sorted_list[mid_index]

        # work with right half
        if sought_value > mid_value:
            return binary_search_recursive(sorted_list, first_index=mid_index + 1, last_index=last_index, sought_value=sought_value)

        # work with left half
        if sought_value < mid_value:
            return binary_search_recursive(sorted_list, first_index, last_index=mid_index - 1, sought_value=sought_value)

        # match found!
        return mid_index


# list to search through
sorted_list = [1, 3, 5, 7, 8, 10, 22, 45, 87]

# results
print(binary_search(sorted_list, 6))
print(binary_search(sorted_list, 45))
print(binary_search_recursive(sorted_list, 0, 8, 10))
print(binary_search_recursive(sorted_list, 0, 8, 99))

# Binary search, O(log n), is faster than linear search except for small arrays, but the array must be sorted first.
# Best case (space complexity) : O(1) Note that this is more if recursion is opted for above.
# Average case : O(log n)
# Worst case : O(log n)
# O(log n) is actually very good!!!
# Any algorithm that cuts the problem in half each time is O(log n)

# The concern here is the number of steps it will take to possibly reach/find the sought-after value
# If the list has:
# a) 2 elements, split 1 time and there's only 1 element to look at
# b) 4 elements, split 2 times
# c) 8 elements, split 3 times
# d) 16 elements, split 4 times
# e) 32 elements, split 5 times
# The split-count increases by 1 as the number of elements doubles

# So, for a sorted list of n elements, the items pending checking for each comparison are:
# a) 1 comparison, n/2 items
# b) 2 comparisons, n/4 items
# c) 3 comparisons, n/8 items
# d) 4 comparisons, n/16 items
# e) 5 comparisons, n/32 items
# Basically, for 32 items, 32 = 2^5, hence 5 steps are taken
# That is, raise 2 to the power of the number of steps
# Logarithms are the inverse of exponential functions,
# The inverse of y = 2^x is y = log base 2 of x
# For 32 items, log n = log 32 = log 2^5
# To get to one item in a list of 32, 1 = 32/32 = 32 * 1/(2^5)
# That is, 1 = n * 1/(2^x), so n = 2^x, which is log base 2 of n = x

# As n doubles, the algorithm will take extra time (t) to run.
# t does not double but increases by a constant amount,
# and won't cause worry for larger values of n