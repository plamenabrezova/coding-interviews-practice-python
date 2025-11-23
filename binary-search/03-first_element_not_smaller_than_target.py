# Given an array of integers sorted in increasing order and a target,
# find the index of the first element in the array that is larger than or equal to the target.
# Assume that it is guaranteed to find a satisfying number.

# Input:
# arr = [1, 3, 3, 5, 8, 8, 10]
# target = 2
# Output: 1
# Explanation: the first element larger than 2 is 3 which has index 1.

# Input:
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: 3
# Explanation: the first element larger than 6 is 7 which has index 3.

# The feasible function here is arr[i] >= target.
from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    start, end = 0, len(arr) - 1
    result = float('inf')

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result if result != float('inf') else -1


if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # target = int(input())
    # res = first_not_smaller(arr, target)
    # print(res)
    print(first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6))
    print(first_not_smaller([1, 3, 3, 5, 8, 8, 10], 2))
