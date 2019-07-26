"""
Heap Sort is based on Binary Heap data structure.
Similar to selection sort; find the maximum element and place it at the end.
Then repeat for the remaining elements.

It cab be used to:
> Sort a nearly sorted or K-sorted array.
> Find k largest or smallest elements in an array.
`k` simply represents a condition

A Complete Binary Tree is one in which every level (except possibly the last)
is completely filled and all nodes are as far left as possible.

A Binary Heap is a Complete Binary Tree where items are stored in a special order
such that the value in a parent node is greater (called a max heap) or smaller (min heap)
than both values in its child nodes.

Work with the heap as a Binary Tree or an Array, using either the max or the min heap ordering.
Representation as an Array is more space efficient.
> Parent node at index i
> Left child at index (2*i) + 1
> Right child at index (2*i) + 2

Doing a heap sort in ascending/increasing order:
> Create a max heap from data, meaning that the largest item is at the root.
> Replace it with the last item of the heap followed by reducing the size of heap by 1.
> Then, heapify the root of tree.
> Repeat the steps while the heap size > 1.

To heapify, the node's children must've already been heapified,
so the action is done in bottom-up order.
That is, (right < left < root), starting with the children.

No. of leaves expected in a binary tree is (floor(n/2) + 1) up to n
"""


def max_heapify(data, heap_size, index_sub_tree):
    """
    Build a max heap by organising a sub-tree such that:
    > the root contains the maximum element
    > the left sub-tree is a max heap
    > the right sub-tree is a max heap
    """

    index_largest = index_sub_tree  # set largest as the value of root
    index_left = (2 * index_sub_tree) + 1
    index_right = (2 * index_sub_tree) + 2

    # check if left exists and is > root, and reassign value of root index
    if (index_left < heap_size) and (data[index_left] > data[index_sub_tree]):
        index_largest = index_left

    # check if right exists and is > index_largest, and reassign value of root index
    if (index_right < heap_size) and (data[index_right] > data[index_largest]):
        index_largest = index_right

    # if the largest element is not at the root of the sub-tree, swap and heapify!
    if index_largest != index_sub_tree:
        # swap
        data[index_sub_tree], data[index_largest] = data[index_largest], data[index_sub_tree]

        # heapify at the largest index
        max_heapify(data, heap_size, index_largest)


def heap_sort(data):
    heap_size = len(data)

    # create a max heap
    # loop indices in reverse
    # heapify at each index/sub-tree
    for i in range(heap_size, -1, -1):
        # deal with the lowest nodes first
        max_heapify(data, heap_size, index_sub_tree=i)
        # print(data, 'heapified')

    # loop indices in reverse
    # perform a swap with the 1st element in the heap for each element
    # heapify after each swap
    # print(data, 'after first run')
    for i in range(heap_size-1, 0, -1):
        # swap the 1st and last node, and remove the last node from the heap
        data[i], data[0] = data[0], data[i]

        # create a max heap from the new/reduced array
        max_heapify(data, heap_size=i, index_sub_tree=0)
        # print(data, 'swapped and heapified', i)

    return data


# list to sort
data = [64, 34, 25, 12, 22, 11, 90]

# results
print(heap_sort(data))  # [11, 12, 22, 25, 34, 64, 90]


# Heapification?
#
# Consider working with the max heap (indices are in brackets):

# 1. For the 1st for-loop
#
#         64(0)                                            64(0)          max in node 0 is 90           90(0)
#     /           \                                    /           \     ---------------------->    /           \
#   34(1)         25(2)     max in node 2 is 90      34(1)         90(2)           swap          34(1)         64(2)
#   /    \        /    \   ---------------------->   /    \        /    \                        /    \        /    \
# 12(3)  22(4)  11(5)  90(6)         swap          12(3)  22(4)  11(5)  25(6)                  12(3)  22(4)  11(5)  25(6)
#
# [90, 34, 64, 12, 22, 11, 25]

# 2. For the 2nd for-loop

# i = 6
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (25, 90) = (90, 25) reflects into
#
#         25(0)          max in node 0 is 64           64(0)
#     /           \     ---------------------->    /           \
#   34(1)         64(2)           swap          34(1)         25(2)
#   /    \        /                             /    \        /
# 12(3)  22(4)  11(5)                         12(3)  22(4)  11(5)
#
# [64, 34, 25, 12, 22, 11, 90]

# i = 5
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (11, 64) = (64, 11) reflects into
#
#         11(0)          max in node 0 is 34           34(0)                                          34(0)
#     /           \     ---------------------->    /           \                                  /           \
#   34(1)         25(2)           swap          11(1)         25(2)     max in node 1 is 22     22(1)         25(2)
#   /    \                                      /    \                ---------------------->   /    \
# 12(3)  22(4)                                12(3)  22(4)                                    12(3)  11(4)
#
# [34, 22, 25, 12, 11, 64, 90]

# i = 4
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (11, 34) = (34, 11) reflects into
#
#         11(0)          max in node 0 is 25           25(0)
#     /           \     ---------------------->    /           \
#   22(1)         25(2)           swap          22(1)         11(2)
#   /                                           /
# 12(3)                                       12(3)
#
# [25, 22, 11, 12, 34, 64, 90]

# i = 3
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (12, 25) = (25, 12) reflects into
#
#         12(0)          max in node 0 is 22           22(0)
#     /           \     ---------------------->    /           \
#   22(1)         11(2)           swap          12(1)         11(2)
#
# [22, 12, 11, 25, 34, 64, 90]

# i = 2
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (11, 22) = (22, 11) reflects into
#
#    11(0)    max in node 0 is 12     12(0)
#   /        ---------------------->  /
# 12(1)                             11(1)
#
# [12, 11, 22, 25, 34, 64, 90]

# i = 1
# swap the 1st and last node, and remove the last node from the heap
# data[i], data[0] = data[0], data[i]
# so (11, 12) = (12, 11) reflects into
#
#    11(0)  algorithm ends here!
#
# [11, 12, 22, 25, 34, 64, 90]

# Complexity
# Space complexity is O(1) and it sorts in place
# If the heap has to be built during heapification, it takes O(n) at worst
