# A sorted array of unique integers was rotated at an unknown pivot.
# For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20].
# Find the index of the minimum element in this array.
#
# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: the smallest element is 10 and its index is 3.
#
# Input: [3, 5, 7, 11, 13, 17, 19, 2]
# Output: 7
# Explanation: the smallest element is 2 and its index is 7.

# At first glance, it seems that there's no way to do it in less than linear time. The array is not sorted.
# But remember binary search can work beyond sorted arrays,
# as long as there is a binary decision we can use to shrink the search range.

# Notice the numbers are divided into two sections: numbers larger than the last element of the array
# and numbers smaller than it.
# The minimum element is at the boundary between the two sections.
# We can apply a feasible function of < the last element and get the boolean array that characterizes the two sections.

# Now the problem is yet again reduced to finding the first true element in a boolean array.
from typing import List


def find_min_rotated(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid - 1] > arr[mid]:
            return mid
        else:
            if mid + 1 <= len(arr) - 1:
                if arr[mid] <= arr[mid + 1]:
                    start = mid + 1
                else:
                    return mid + 1
            else:
                break
    return 0


def find_min_rotated_v2(arr) -> int:
    stat, end = 0, len(arr) - 1
    result = 0

    while stat <= end:
        mid = (stat + end) // 2

        if arr[mid] <= arr[-1]:
            result = mid
            end = mid - 1
        else:
            stat = mid + 1

    return result


if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # res = find_min_rotated(arr)
    # print(res)
    print(find_min_rotated([3, 5, 7, 11, 13, 17, 19, 2]))
    print(find_min_rotated([30, 40, 50, 10, 20]))
    print(find_min_rotated([0, 1, 2, 3, 4, 5]))
    print(find_min_rotated([0]))
    print(find_min_rotated([1, 2, 3, 5, 8, 0]))
    # second version
    print('---------------')
    print(find_min_rotated_v2([3, 5, 7, 11, 13, 17, 19, 2]))
    print(find_min_rotated_v2([30, 40, 50, 10, 20]))
    print(find_min_rotated_v2([0, 1, 2, 3, 4, 5]))
    print(find_min_rotated_v2([0]))
    print(find_min_rotated_v2([1, 2, 3, 5, 8, 0]))