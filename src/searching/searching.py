# STRETCH: implement Linear Search
def linear_search(arr, target):
    nums = 0
    while True:
        if arr[nums] == target
        return true
        else:
            nums += 1
        # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    low = 0
    high = len(arr)-1
    mid = low + high // 2
    # TO-DO: add missing code
    while arr[mid] != target:
        if arr[mid] < target:
            mid -= 1
        elif arr[mid] > target:
            mid += 1

    if arr[mid] == target:
        return arr[mid]
    return -1  # not found
# function binary_search_iterative(arr, target){
#   // move low and high depends if target < midpoint
#   let low = 0
#   let high = arr.length - 1
#   while (low <= high) {
#     let mid = Math.floor(low + high) / 2
#     if (target === arr[mid] ) {
#       return `found ${target} == ${true} at index  ${mid}`
#     } else if (target < arr[mid]) {
#         high = mid -1
#     } else {
#       low = mid + 1
#     }
#   }
#   return false
# }

# js version
# function binary_search(arr, target){
#   if(arr.length === 0){
#     return -1
#   }
#   const low = 0
#   const high = arr.length - 1
#   let mid = low + high / 2

# // 1. Compare the item in the middle of the data set to the item we are searching for.
# //     - If it is the same, stop. We found it and are done!
# while (arr[mid] !== target){
#   if (target < arr[mid]){
#     mid -= 1
#   } else if (target > arr[mid]){
#     mid += 1
#    }
#   }
#   if(arr[mid] === target){
#     return arr[mid]
#   }

#   return -1
# }
# binary_search([ 1, 2, 3, 4, 5], 5)

# STRETCH: write a recursive implementation of Binary Search
#     def binary_search_recursive(arr, target, low, high):
    print(arr)
    mid = (low + high) // 2
    if low > high:
        return -1
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return bsr(arr, target, low, mid - 1)
    else:
        return bsr(arr, target, mid + 1, high)


test = [1, 2, 3, 12, 5, 6, 21, 22]
print(bsr(test, 12, 0, len(test) - 1))
