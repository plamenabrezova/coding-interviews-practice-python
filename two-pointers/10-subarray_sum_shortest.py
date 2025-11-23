# Given a positive integer array nums, we want to find the length of the shortest subarray such that the subarray sum
# is at least target.
# Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10,
# then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.
# We'll assume for this problem that it's guaranteed target will not exceed the sum of all elements in nums.

from typing import List

def subarray_sum_shortest(nums: List[int], target: int) -> int:
    window_sum, result = 0, len(nums)
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            result = min(result, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return result

if __name__ == '__main__':
    print(subarray_sum_shortest([1, 4, 1, 7, 3, 0, 2, 5], 10))
