from collections import Counter

def singleNumber(nums) -> int:

    # counter_nums = Counter(nums)
    # counter_nums = sorted(counter_nums.keys(), key=lambda v: counter_nums[v])
    # return int(counter_nums[0])


    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]

    return result


print(singleNumber([2, 2, 1]))
print(singleNumber([4,1,2,1,2]))