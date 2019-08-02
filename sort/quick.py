"""
Quick Sort aka partition-exchange sort is an efficient sorting algorithm
serving as a systematic method for placing the elements of a random access file
or an array in order.
> It is a Divide and Conquer algorithm.
> It is a comparison sort.
> It can operate in-place on an array.
> Similar to selection sort but doesn't always choose the worst-case partition.

When implemented well, it can be twice or thrice as fast as its main competitors,
merge sort and heapsort.

How it works - pick an element as a pivot and partition the array around this pivot.
The pivot element can be can chosen as the:
1. First.
2. Last.
3. Random.
4. Median.

The idea is partitioning an array by placing elements smaller than the pivot before the pivot
and those larger after the pivot.
"""


def partition(data, low_index, high_index):
    """
    Using the last element as the pivot, place smaller elements to the left
    and larger ones to the right, then return the next index to pivot
    """

    index_smaller = low_index - 1
    pivot = data[high_index]

    for i in range(low_index, high_index):

        # if current element is <= pivot
        if data[i] <= pivot:
            index_smaller += 1

            # swap current index and the smaller index
            data[index_smaller], data[i] = data[i], data[index_smaller]

    # swap highest index with index after index_smaller
    data[index_smaller + 1], data[high_index] = data[high_index], data[index_smaller + 1]
    return index_smaller + 1


def quick_sort(data, low_index, high_index):
    if low_index < high_index:
        pivot_index = partition(data, low_index, high_index)

        # sort both partitions around the pivot
        quick_sort(data, low_index, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high_index)

    return data


# list to sort
data = [64, 90, 25, 12, 22, 11, 34]

# results
n = len(data)
print(quick_sort(data, 0, n-1))  # [11, 12, 22, 25, 34, 64, 90]

# How it works

# 1. partition() function runs for O(n)
# if data = [64, 90, 25, 12, 22, 11, 34], low_index = 0, high_index = 6
# then index_smaller = -1, pivot = 34

# i = 0, data[i] = 64, data[i] <= pivot so index_smaller = 0
# swap (64, 64) = (64, 64)
# [64, 90, 25, 12, 22, 11, 34]

# i = 1, data[i] = 90, data[i] > pivot

# i = 2, data[i] = 25, data[i] <= pivot so index_smaller = 1
# swap (90, 25) = (25, 90)
# [64, 25, 90, 12, 22, 11, 34]

# i = 3, data[i] = 12, data[i] <= pivot so index_smaller = 2
# swap (90, 12) = (12, 90)
# [64, 25, 12, 90, 22, 11, 34]

# i = 4, data[i] = 22, data[i] <= pivot so index_smaller = 3
# swap (90, 22) = (22, 90)
# [64, 25, 12, 22, 90, 11, 34]

# i = 5, data[i] = 11, data[i] <= pivot so index_smaller = 4
# swap (90, 11) = (11, 90)
# [64, 25, 12, 22, 11, 90, 34]

# outside the for-loop
# data[5], data[6] = data[6], data[5]
# swap (90, 34) = (34, 90)
# [64, 25, 12, 22, 11, 34, 90]


# 2. quick_sort() function
# pivot_index = 4, pivot = 34
# [25, 12, 22, 11, 34, 90, 64])

# pivot_index = 0, pivot = 25
# [11, 12, 22, 25, 34, 90, 64]

# pivot_index = 3, pivot = 25
# [11, 12, 22, 25, 34, 90, 64]

# pivot_index = 2, pivot = 22
# [11, 12, 22, 25, 34, 90, 64]

# pivot_index = 5, pivot = 90
# [11, 12, 22, 25, 34, 64, 90]

# Complexity
# Worst case - O(n^2) when greatest or smallest element is the pivot
# Best case - O(n * log n) when the middle element is selected
# Average case - O(n * log n)