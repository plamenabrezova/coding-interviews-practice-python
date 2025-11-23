# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import Counter

def single_number_counter_collection(nums) -> int:
    counter_nums = Counter(nums)
    counter_nums = sorted(counter_nums.keys(), key=lambda v: counter_nums[v])
    return int(counter_nums[0])

def single_number_xor_function(nums) -> int:
    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]
    return result

print(single_number_counter_collection([2, 2, 1]))
print(single_number_counter_collection([4,1,2,1,2]))

print(single_number_xor_function([2, 2, 1]))
print(single_number_xor_function([4,1,2,1,2]))