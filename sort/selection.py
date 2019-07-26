"""
Sort an array by repeatedly finding the minimum element (in ascending order)
in the unsorted part and transfering it to the beginning.
It works with 2 sub-arrays; the sorted and the unsorted.
"""


def selection_sort(data):
    len_data = len(data)

    for i in range(len_data):
        min_index = i

        # the unsorted array (elements beyond i)
        for j in range(i+1, len_data):
            if data[min_index] > data[j]:
                min_index = j

        # having set the min_index above, perform a swap
        data[i], data[min_index] = data[min_index], data[i]
    return data


# list to sort
data = [64, 34, 25, 12, 22, 11, 90]

# results
print(selection_sort(data))  # [11, 12, 22, 25, 34, 64, 90]

# how it works
# i = min_index = 0
# j = 1, data[min_index] = 64, data[j] = 34, data[min_index] > data[j], so min_index = 1
# j = 2, data[min_index] = 34, data[j] = 25, data[min_index] > data[j], so min_index = 2
# j = 3, data[min_index] = 25, data[j] = 12, data[min_index] > data[j], so min_index = 3
# j = 4, data[min_index] = 12, data[j] = 22, but data[min_index] < data[j]
# j = 5, data[min_index] = 12, data[j] = 11, data[min_index] > data[j], so min_index = 5
# j = 6, data[min_index] = 11, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 11 and data[min_index] = 64
# [11, 34, 25, 12, 22, 64, 90]

# i = min_index = 1
# j = 2, data[min_index] = 34, data[j] = 25, data[min_index] > data[j], so min_index = 2
# j = 3, data[min_index] = 25, data[j] = 12, data[min_index] > data[j], so min_index = 3
# j = 4, data[min_index] = 12, data[j] = 22, but data[min_index] < data[j]
# j = 5, data[min_index] = 12, data[j] = 64, but data[min_index] < data[j]
# j = 6, data[min_index] = 12, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 12 and data[min_index] = 34
# [11, 12, 25, 34, 22, 64, 90]

# i = min_index = 2
# j = 3, data[min_index] = 25, data[j] = 34, but data[min_index] < data[j]
# j = 4, data[min_index] = 25, data[j] = 22, data[min_index] > data[j], so min_index = 3
# j = 5, data[min_index] = 22, data[j] = 64, but data[min_index] < data[j]
# j = 6, data[min_index] = 22, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 22 and data[min_index] = 34
# [11, 12, 22, 34, 25, 64, 90]

# i = min_index = 3
# j = 4, data[min_index] = 34, data[j] = 25, data[min_index] > data[j], so min_index = 4
# j = 5, data[min_index] = 25, data[j] = 64, but data[min_index] < data[j]
# j = 6, data[min_index] = 25, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 22 and data[min_index] = 34
# [11, 12, 22, 25, 34, 64, 90]

# i = min_index = 4
# j = 5, data[min_index] = 34, data[j] = 64, but data[min_index] < data[j]
# j = 6, data[min_index] = 34, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 34 and data[min_index] = 34
# [11, 12, 22, 25, 34, 64, 90]

# i = min_index = 5
# j = 6, data[min_index] = 64, data[j] = 90, but data[min_index] < data[j]
# perform swap so data[i] = 64 and data[min_index] = 64
# [11, 12, 22, 25, 34, 64, 90]

# Complexity
# The first for loop runs n times whereas the inner one runs (n-1) times
# That is O(n * (n-1)) which is O(n^2)
# Space complexity is O(1) and it sorts in place