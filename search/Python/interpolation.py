"""
Interpolation search works better than Binary Search for sorted and uniformly distributed arrays.
log(log n) comparisons are made if the above condition is met, but at worst O(n) comparisons.
This is basically an improvement over Binary Search for the above conditions.

The difference here is that instead of using the mid_index,
the position to be compared with is determined by comparing the sought value
to the first and last values in the list, and working with the closest to the sought value.

So, return a higher value of position when element to be searched is closer to data[last_index].
And a smaller value when closer to data[first_index]
position = first_index + [ (sought_value - data[first_index]) * \
                            (last_index - first_index) / (data[last_index] - data[first_index]) ]
"""


def interpolation_search(sorted_list, sought_value):
    """Return the index of the sought value in the sorted list"""

    first_index = 0
    last_index = len(sorted_list) - 1

    while first_index <= last_index and sought_value <= sorted_list[last_index]:

        # check for match if it's a one-item list
        if first_index == last_index:
            if sorted_list[first_index] == sought_value:
                return first_index

        # get the position to be used
        position = first_index + (
            (sought_value - sorted_list[first_index]) *
            int(float(last_index - first_index) /
                (sorted_list[last_index] - sorted_list[first_index]))
        )

        # match found!
        if sorted_list[position] == sought_value:
            return position

        # work with right section of list
        if sought_value > sorted_list[position]:
            first_index = position + 1
        else:
            # work with left section of list
            last_index = position - 1

    # no match
    return None


# list to search through
sorted_list = [1, 3, 5, 7, 8, 10, 22, 45, 87]

# results
print(interpolation_search(sorted_list, 6))  # None
print(interpolation_search(sorted_list, 45))  # 7

# For details on complexity, see:
# 1. https://www.cadmo.ethz.ch/education/lectures/HS18/SAADS/reports/17.pdf
# 2. http://webcache.googleusercontent.com/search?q=cache:http://www.cs.technion.ac.il/~itai/publications/Algorithms/p550-perl.pdf