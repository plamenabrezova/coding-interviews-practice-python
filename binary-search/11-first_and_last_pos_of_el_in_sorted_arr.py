# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
#
# Example 2:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
#
# Example 3:
# Input: nums = [], target = 0
# Output: [-1, -1]

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    first_idx, last_idx = -1, -1

    # find first position
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            first_idx = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # find last position
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            last_idx = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return [first_idx, last_idx]


print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
print(search_range([2, 2], 2))