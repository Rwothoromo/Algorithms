"""
Insertion sort build the sorted list one item at a time.
This is a problem if the list to be sorted is large!
It works the same way playing cards are sorted in one's hands.

It is O(n^2) and:
1. Efficient for small data sets.
2. More efficient than most O(n^2) algorithms, for example Selection Sort and Bubble Sort.
3. Online (can sort a list as it receives it).
"""


def insertion_sort(data):
    # loop starting from the 2nd element
    # print(data, 'b4')
    for i in range(1, len(data)):
        key = data[i]

        # check if the previous element is greater than the key
        # move the found element, if condition suffices, to the start of the list
        j = i - 1  # previous index
        while j >= 0 and key < data[j]:
            # set the value present value as the key
            data[j + 1] = data[j]
            # print(data, 'now', j)
            j -= 1

        # set the present value as the key
        data[j + 1] = key
        # print(data, 'aft', j)
    return data


# list to sort
data = [64, 34, 25, 12, 22, 11, 90]

# results
print(insertion_sort(data))  # [11, 12, 22, 25, 34, 64, 90]

# how it works
# i = 1, key = 34, j = 0, data[j] = 64
# key < data[j] so data[j + 1] = data[j] hence 34 becomes 64
# [64, 64, 25, 12, 22, 11, 90]
# then j = -1, data[j + 1] = key, so 64 becomes 34
# [34, 64, 25, 12, 22, 11, 90]

# i = 2, key = 25, j = 1, data[j] = 64
# key < data[j] so data[j + 1] = data[j] hence 25 becomes 64
# [34, 64, 64, 12, 22, 11, 90]
# then j = 0, data[j + 1] = data[j], so 64 becomes 34
# [34, 34, 64, 12, 22, 11, 90]
# then j = -1, data[j + 1] = key, so 34 becomes 25
# [25, 34, 64, 12, 22, 11, 90]

# i = 3, key = 12, j = 2, data[j] = 64
# key < data[j] so data[j + 1] = data[j] hence 12 becomes 64
# [25, 34, 64, 64, 22, 11, 90]
# then j = 1, data[j + 1] = data[j], so 64 becomes 34
# [25, 34, 34, 64, 22, 11, 90]
# then j = 0, data[j + 1] = data[j], so 34 becomes 25
# [25, 25, 34, 64, 22, 11, 90]
# then j = -1, data[j + 1] = key, so 25 becomes 12
# [12, 25, 34, 64, 22, 11, 90]

# i = 4, key = 22, j = 3, data[j] = 64
# key < data[j] so data[j + 1] = data[j] hence 22 becomes 64
# [12, 25, 34, 64, 64, 11, 90]
# then j = 2, data[j + 1] = data[j], so 64 becomes 34
# [12, 25, 34, 34, 64, 11, 90]
# then j = 1, data[j + 1] = data[j], so 34 becomes 25
# [12, 25, 25, 34, 64, 11, 90]
# then j = 0, but key > data[j]
# data[j + 1] = key, so 25 becomes 22
# [12, 22, 25, 34, 64, 11, 90]

# i = 5, key = 11, j = 4, data[j] = 64
# key < data[j] so data[j + 1] = data[j] hence 11 becomes 64
# [12, 22, 25, 34, 64, 64, 90]
# then j = 3, data[j + 1] = data[j], so 64 becomes 34
# [12, 22, 25, 34, 34, 64, 90]
# then j = 2, data[j + 1] = data[j], so 34 becomes 25
# [12, 22, 25, 25, 34, 64, 90]
# then j = 1, data[j + 1] = data[j], so 25 becomes 22
# [12, 22, 22, 25, 34, 64, 90]
# then j = 0, data[j + 1] = data[j], so 22 becomes 12
# [12, 12, 22, 25, 34, 64, 90]
# then j = -1, data[j + 1] = key, so 12 becomes 11
# [11, 12, 22, 25, 34, 64, 90]

# i = 6, key = 90, j = 5, data[j] = 64
# but key > data[j]
# data[j + 1] = key, so 90 becomes 90 #:D
# [11, 12, 22, 25, 34, 64, 90]

# Complexity
# The for loop runs for O(n-1)
# The while loop is dependent on a condition and runs for f(n)
# The complexity is O(n + f(n))
# If f(n) is O(n), the algorithm runs for O(n)
# At the worst, it runs for n(n-1)/2, giving O(n^2)

# How?
# If the list is sorted in reverse, for example, [90, 64, 34, 25, 22, 12, 11]
# When insert is called the first time, k = 1
# This continues until k = n-1, hence in looping through the k's:
# c*1 + c*2 + ... + c*(n-1) = c(1 + 2 + ... + (n-1))
# This is like the formula for arithmetic series (n+1)(n/2), but with n as (n-1):
# Hence, c(n-1+1)((n-1)/2) = c(n^2 - n)/2
# That is, O(n^2)