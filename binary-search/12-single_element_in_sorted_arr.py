# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

# Observe that the parity (even or odd) of indices ties closely with where the single element is.
# We know that the numbers come in pairs before and after the one single element s.
# For the pairs that is to the left of s: the first element takes an even index e (as array is 0 indexed)
# and the second element takes an odd index e+1. Then the single element s takes only one position (even),
# so that the pattern on the right of s is reversed.
# For the pairs that is to the right of s: the first element takes an odd index o,
# and the second element takes an even index 0+1
#
# Therefore, for an even index e, nums[e]!=nums[e+1] if the s is to the left of 0.
# Similar for an odd index o, nums[o]!=nums[o-1] means s has already appeared.
# We must also keep an eye out for out of bounds, that is, to check whether idx is the last index in nums.

# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


def to_the_left(arr, idx) -> bool:

    if idx == len(arr) - 1:
        return True
    elif idx % 2:
        return arr[idx] != arr[idx - 1]
    else:
        return arr[idx] != arr[idx + 1]


def single_non_duplicate(nums: List[int]) -> int:
    start, end, result = 0, len(nums) - 1, -1

    while start <= end:
        mid = (start + end) // 2

        if to_the_left(nums, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return nums[result]


print(single_non_duplicate([1,1,2,3,3,4,4,8,8]))
