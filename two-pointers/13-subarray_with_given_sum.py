# Given an array of integers and an integer target, find a subarray that sums to target and return the start and end
# indices of the subarray.

# Input: arr: 1 -20 -3 30 5 4 target: 7
# Output: 1 4
# Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).

from typing import List
from collections import Counter

def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sum = {0: 0}
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        complement = current_sum - target
        if complement in prefix_sum:
            return [prefix_sum[complement], i + 1]
        prefix_sum[current_sum] = i + 1

def subarray_sum_total(arr: List[int], target: int) -> int:
    prefix_sum = Counter()
    prefix_sum[0] = 1
    current_sum = 0
    result = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        complement = current_sum - target
        if complement in prefix_sum:
            result += prefix_sum[complement]
        prefix_sum[current_sum] += 1

    return result

input_arr = [1, -20, -3, 30, 5, 4]
print(subarray_sum(input_arr, 7))
print(subarray_sum_total(input_arr, 7))