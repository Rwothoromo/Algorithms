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

# Binary search is faster than linear search except for small arrays, but the array must be sorted first.
# Space Complexity is O(n)
# Worst case space complexity is O(1)
# Best case performance is O(1)
# Average case performance is O(log n)
# Worst case performance is O(log n)