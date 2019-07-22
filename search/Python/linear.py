"""
By going through each item in a data structure till the sought item is found,
a Linear search is performed. It is of course, rarely used because it's inefficient.
"""


def linear_search(data, sought_value):
    """Return True if the sought value is in the data"""

    data_len = len(data)
    for i in range(0, data_len):
        if data[i] == sought_value:
            return True
    return False


# list to search through
data = [10, 7, 8, 9, 22, 15, 87]

# results
print(linear_search(data, 3))  # False
print(linear_search(data, 9))  # True

# Worst case (space complexity) : O(1)
# Best case : O(1) (if sought value is the first element)
# Average case : O(n)
# Worst case : O(n) (if sought value is not in the data)
# Any algorithm that iterates through all data once is pretty much O(n)
