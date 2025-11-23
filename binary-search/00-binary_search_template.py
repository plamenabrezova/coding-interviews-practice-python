# A monotonic function is a function that is either non-decreasing or non-increasing.
# Given x1 and x2 where x1 > x2, we should have f(x1) >= f(x2).

# A sorted array is monotonic because the value increases or stays the same as the index increases.

# If f(x) only contain boolean values True and False and think true as 1 and false as 0,
# then a sorted boolean array would consist of consecutive 0s and then consecutive 1s. For example, FFFFTTTTT.

# Binary Search Template:
# feasible function:
# The pre-condition for binary search is to find a monotonic function f(x) that returns either True or False.
# Then the problem becomes Find the First True in a Sorted Boolean Array.
# We will call the function feasible to signify that whether the element at the current index is feasible (True)
# or not (False) to meet the problem constraints.

# Now the problem has become finding the feasible function and then mechanically applying the template.
# For example: in the 'Find the First True in a Sorted Boolean Array' problem,
# the feasible function is simply arr[mid] is True.
# It's trickier to find the feasible function in other problems.
from typing import List

def feasible(mid: int) -> bool:
    pass


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1

    while left <= right:
        mid = (left + right) // 2

        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
