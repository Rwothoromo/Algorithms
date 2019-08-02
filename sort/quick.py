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
data = [64, 34, 25, 12, 22, 11, 90]

# results
n = len(data)
print(quick_sort(data, 0, n-1))  # [11, 12, 22, 25, 34, 64, 90]
