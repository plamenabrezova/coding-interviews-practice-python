# Fixed size sliding window template
# def sliding_window_fixed(input, window_size):
#     ans = window = input[0:window_size]
#     for right in range(window_size, len(input)):
#         left = right - window_size
#         remove input[left] from window
#         append input[right] to window
#         ans = optimal(ans, window)
#     return ans

from typing import List

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    p1, p2 = 0, k - 1

    result = 0
    while p2 < len(nums):
        result = max(result, sum(nums[p1: p2 + 1]))
        p1 += 1
        p2 += 1
    return result

def second_version(nums: List[int], k: int) -> int:
    p2 = k
    init_sum = sum(nums[0: p2])
    result = init_sum

    while p2 < len(nums):
        p1 = p2 - k
        init_sum -= nums[p1]
        init_sum += nums[p2]
        result = max(init_sum, result)
        p2 += 1

    return result


if __name__ == '__main__':
    # nums = [int(x) for x in input().split()]
    # k = int(input())
    # res = subarray_sum_fixed(nums, k)
    # print(res)
    print(subarray_sum_fixed([1, 2, 3, 7, 4, 1], 3))
    print(second_version([1, 2, 3, 7, 4, 1], 3))
