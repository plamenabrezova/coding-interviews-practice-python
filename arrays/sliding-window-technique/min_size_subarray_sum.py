def minSubArrayLen(target, nums) -> int:
    if sum(nums) < target:
        return 0

    min_length = len(nums)

    for start in range(len(nums)):
        end = start
        res = nums[start]

        while res < target and end < len(nums) - 1:
            end += 1
            res += nums[end]

        if res >= target:
            if start == end:
                min_length = 1
            else:
                min_length = min(min_length, end - start + 1)

    return min_length

#nums = [2,3,1,2,4,3]
#print(minSubArrayLen(7, nums))
#nums = [1,2,3,4,5]
#print(nums.index(max(nums)))
#print(nums[0:nums.index(max(nums))] + nums[nums.index(max(nums)):-1])
#print(minSubArrayLen(11, nums))

# def minSub(target, nums):
#     if sum(nums) < target:
#         return 0
#
#     min_length = len(nums)
#     res = 0
#     idx = 0
#     n = nums
#     while res < target:
#         res += max(n)
#         idx += 1
#         n = n[0:n.index(max(n))] + n[n.index(max(n)):-1]
#
#     min_length = idx
#     return min_length


# nums = [1,2,3,4,5]
# print(minSub(11, nums))

## SOME TESTING
# nums = [12,28,83,4,25,26,25,2,25,25,25,12]
# print(sum(nums))
#
# nums = [12,28,83,4,25,26,25,2,25,25,25]
# print(sum(nums))
#
# nums = [28,83,4,25,26,25,2,25,25,25]
# print(sum(nums))
#
# nums = [28,83,4,25,26,25,2,25,25]
# print(sum(nums))
#
# nums = [28,83,4,25,26,25,2,25]
# print(sum(nums))
# print(len(nums))


def find_window_dimensions(n, start, end, s, e):
    if n[s] > n[e]:
        return start, end - 1
    elif n[s] < n[e]:
        return start + 1, end
    else:
        if s + 1 != e and s + 1 != e - 1:
            return find_window_dimensions(n, start, end, s+1, e-1)
        else:
            return start + 1, end


def min_sub_sum(target, nums):
    res = sum(nums)
    if res < target:
        return 0
    start = 0
    end = len(nums) - 1
    min_length = len(nums)
    n = nums

    while res >= target and start != end:
        if sum(n[start + 1: end + 1]) > sum(n[start: end]): # or sum(n[start + 1: end + 1]) == sum(n[start: end]):
            start += 1
        elif sum(n[start + 1: end + 1]) < sum(n[start: end]):
            end -= 1
        else:
            if n[start + 1] < n[end - 1]:
                start += 1
            else:
                end -= 1

        substring = n[start:end + 1]
        res = sum(substring)
        if res >= target:
            min_length = min(min_length, end - start + 1)

    return min_length

#nums = [12,28,83,4,25,26,25,2,25,25,25,12]
nums = [2,3,1,2,4,3]
print(enumerate(nums))
for r in enumerate(nums):
    print(r)
#print(min_sub_sum(7, nums))
#nums = [5,1,3,5,10,7,4,9,2,8]
#print(min_sub_sum(15, nums))

#nums = [1,1,1,1,7]
#print(min_sub_sum(7, nums))