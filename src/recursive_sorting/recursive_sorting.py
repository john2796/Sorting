# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    if len(arrA) > 0:
        return merge(arrA, arrB)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr) / 2
        left = merge_sort(arr[0: mid])
        right = merge_sort(arr[mid:])
    arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# from time import time

# import random

# l = [random.randint(0,1000) for i in range(0,100)]

# print(l)

# def quick_sort( arr, low, high ):
#   # base case
#     if low >= high:
#         return arr

#   # Start by choosing a pivot
#   # First or last element is easiest
#   # Middle, median, or random element usually performs better (tends to split original data more evenly)
#     else:
#         # divide
#         pivot_index = low

#         for i in range(low, high):
#           print(arr)
#             # Move all elements smaller than pivot to its left-hand side. Move all elements larger than pivot to its right-hand side.
#           if arr[i] < arr[pivot_index]:
#             temp = arr[pivot_index+1]
#             arr[pivot_index+1] = arr[i]
#             arr[i] = temp

#             # swap pivot with element on its right
#             temp = arr[pivot_index]
#             arr[pivot_index] = arr[pivot_index+1]
#             arr[pivot_index+1] = temp
#             pivot_index +=1

#     # (recursive case) Recursively Quick Sort LHS and RHS until (base case) a side only contains a single element

#     arr = quick_sort(arr, low, pivot_index)

#     arr = quick_sort(arr, pivot_index+1, high)

#     return arr

# # Algorithm to time our code

# # Store a startin time
# start_time = time()

# # Run our code
# quick_sort(l, 0, len(l))
# print(l)

# # Store the ending time
# end_time = time()

# print (end_time - start_time)
