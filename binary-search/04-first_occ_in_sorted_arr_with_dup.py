# Given a sorted array of integers and a target integer,
# find the first occurrence of the target and return its index.
# Return -1 if the target is not in the array.
#
# Input:
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1
# Explanation: The first occurrence of 3 is at index 1.

# Input:
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1
# Explanation: 6 does not exist in the array.

# The feasible function here is arr[mid] >= target
# Caveat: the feasible function checks whether the element is greater than or equal to the target.
# But the question asks for the index of the first element exactly equal to the target.
# Our template updates ans = mid whenever arr[mid] >= target.
# Therefore, we have to make a small modification to the template
# and move ans = mid to only when arr[mid] == target and not arr[mid] >= target.
from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    start, end = 0, len(arr) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            result = mid
            end = mid - 1

        if arr[mid] > target:
            start = mid + 1

        else:
            end = mid - 1

    return result


if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # target = int(input())
    # res = find_first_occurrence(arr, target)
    # print(res)
    print(find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))

