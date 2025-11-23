# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of
# the non-zero elements. Do this in-place using constant auxiliary space.

# Input:
# [1, 0, 2, 0, 0, 7]
# Output:
# [1, 2, 7, 0, 0, 0]

from typing import List

def move_zeros(nums: List[int]) -> None:
    first, end = 0, 0

    while end < len(nums):
        if end != first and nums[end] != 0:
            nums[first], nums[end] = nums[end], nums[first]
        if nums[first] != 0:
            first += 1
        end += 1

if __name__ == '__main__':
    # input_nums = [int(x) for x in input().split()]
    # move_zeros(input_nums)
    # print(' '.join(map(str, input_nums)))
    input_nums = [1, 0, 2, 0, 0, 7]
    move_zeros(input_nums)
    print(input_nums)