from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    second = 0

    if n > 0:
        for i in range(len(nums1)):
            if second < n and (nums1[i] > nums2[second] or i >= m):
                # if nums1[i] == 0:
                #     nums1[i] = nums2[second]
                #     second += 1
                # else:
                window = m - i
                nums1[i + 1: i + 1 + window] = nums1[i: i + window]
                nums1[i] = nums2[second]
                second += 1
                m += 1

    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)
merge([2, 0], 1, [1], 1)
merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
merge([1, 2, 4, 5, 6, 0], 5, [3], 1)
merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
