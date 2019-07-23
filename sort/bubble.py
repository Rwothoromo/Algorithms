"""
Bubble/Sinking Sort repeatedly steps through a list, compares adjacent pairs
and swaps them if they are not in the right order.
That is, each item bubbles up to where it belongs.
It is rather slow except if the least is mostly sorted.
"""


def bubble_sort(data):
    n = len(data)

    for i in range(n):
        # the last elements left out are already in place
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


# list to sort
data = [64, 34, 25, 12, 22, 11, 90]

# results
print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]

# 1st pass, i = 0, loop j = 0..5
# [34, 64, 25, 12, 22, 11, 90], j = 0
# [34, 25, 64, 12, 22, 11, 90]
# [34, 25, 12, 64, 22, 11, 90]
# [34, 25, 12, 22, 64, 11, 90]
# [34, 25, 12, 22, 11, 64, 90]
# [34, 25, 12, 22, 11, 64, 90], j = 5, No Swap

# 2nd pass, i = 1, loop j = 0..4
# [25, 34, 12, 22, 11, 64, 90]
# [25, 12, 34, 22, 11, 64, 90]
# [25, 12, 22, 34, 11, 64, 90]
# [25, 12, 22, 11, 34, 64, 90]
# [25, 12, 22, 11, 34, 64, 90] # No Swap

# 3rd pass, i = 2, loop j = 0..3
# [12, 25, 22, 11, 34, 64, 90]
# [12, 22, 25, 11, 34, 64, 90]
# [12, 22, 11, 25, 34, 64, 90]
# [12, 22, 11, 25, 34, 64, 90] # No Swap

# 4th pass, i = 3, loop j = 0..2
# [12, 22, 11, 25, 34, 64, 90] # No Swap
# [12, 11, 22, 25, 34, 64, 90]
# [12, 11, 22, 25, 34, 64, 90] # No Swap

# 5th pass, i = 4, loop j = 0..1
# [11, 12, 22, 25, 34, 64, 90]
# [11, 12, 22, 25, 34, 64, 90] # No Swap

# 6th pass, i = 5, loop j = 0
# [11, 12, 22, 25, 34, 64, 90] # No Swap

# Complexity
# For n = 7, it took n - 1 passes/steps
# Within the n - 1 passes, it iterated n - i - 1 times,
# where i was 0 initially
# Big-O is (n-1)(n-1)
# Hence O(n^2)
# Best case is O(n) if the list is sorted
# and the algorithm is altered as below:


def bubble_sort_altered(data):
    n = len(data)
    sorted_flag = True

    for i in range(n):
        # the last elements left out are already in place
        for j in range(0, n-i-1):  # skipped if already sorted!
            if data[j] > data[j+1]:
                sorted_flag = False
                print("Swap here!")
                data[j], data[j+1] = data[j+1], data[j]
        # end the iterations if already sorted
        if sorted_flag:
            print("Already sorted")
            return data
    return data


# list to sort
data = [11, 12, 22, 25, 34, 64, 90]

# results
print(bubble_sort_altered(data))
# "Already sorted"
# [11, 12, 22, 25, 34, 64, 90]
