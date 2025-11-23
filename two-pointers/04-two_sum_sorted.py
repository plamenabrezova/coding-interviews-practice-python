# Given an array of integers sorted in ascending order, find two numbers that add up to a given target.
# Return the indices of the two numbers in ascending order.
# You can assume elements in the array are unique and there is only one solution.
# Do this in O(n) time and with constant auxiliary space.

# Input:
# arr: a sorted integer array
# target: the target sum we want to reach
# Sample Input: [2 3 4 5 8 11 18], 8
# Sample Output: 1 3

from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    start, end = 0, len(arr) - 1

    while start != end:
        comp = arr[start] + arr[end]
        if comp > target:
            end -= 1
        elif comp < target:
            start += 1
        else:
            return [start, end]

    return []


if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # target = int(input())
    # res = two_sum_sorted(arr, target)
    # print(' '.join(map(str, res)))
    print(two_sum_sorted([2, 3, 4, 5, 8, 11, 18], 8))
    print(two_sum_sorted([], 6))