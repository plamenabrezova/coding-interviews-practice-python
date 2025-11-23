# We want to find the length of the longest subarray with sum smaller than or equal to a target.

# Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is
# [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).

# Flexible size sliding window template
# def sliding_window_flexible_longest(input):
#     initialize window, ans
#     left = 0
#     for right in range(len(input)):
#         append input[right] to window
#         while invalid(window):        # update left until window is valid again
#             remove input[left] from window
#             left += 1
#         ans = max(ans, window)        # window is guaranteed to be valid here
#     return ans
# def sliding_window_flexible_shortest(input):
#     initialize window, ans
#     left = 0
#     for right in range(len(input)):
#         append input[right] to window
#         while valid(window):
#             ans = min(ans, window)      # window is guaranteed to be valid here
#             remove input[left] from window
#             left += 1
#     return ans

from typing import List

def subarray_sum_longest(nums: List[int], target: int) -> int:
    start, end = 0, 1
    current_sum = nums[start]
    result = 0
    while end < len(nums):
        while current_sum <= target:
            current_sum += nums[end]
            if current_sum <= target:
                result = max(result, (end - start) + 1)
                end += 1

        while current_sum > target:
            current_sum -= nums[start]
            start += 1
        result = max(result, (end - start) + 1)
        end += 1

    return result

def second_version(nums: List[int], target: int) -> int:
    window_sum, result = 0, 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        result = max(result, right - left + 1)

    return result

if __name__ == '__main__':
    # nums = [int(x) for x in input().split()]
    # target = int(input())
    # res = subarray_sum_longest(nums, target)
    # print(res)
    print(subarray_sum_longest([1, 6, 3, 1, 2, 4, 5], 10))
