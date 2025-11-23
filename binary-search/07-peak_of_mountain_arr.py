# A mountain array is defined as an array that:
# - has at least 3 elements
# - has an element with the largest value called "peak", with index k.
#   The array elements strictly increase from the first element to A[k],
#   and then strictly decreases from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.

# That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k.
# Note that the peak element is neither the first nor the last element of the array.

# Find the index of the peak element. Assume there is only one peak element.
# Input: 0 1 2 3 2 1 0
# Output: 3
# Explanation: the largest element is 3 and its index is 3.

# The array strictly increases until the peak element and then strictly decreases.
# The monotonicity is a strong sign that we can use binary search to find the peak element.

# To use binary search though, we need the entire search range to be strictly increasing or decreasing.
# We need to find the feasible function that returns false for elements up until the peak and true
# from the peak to the end.

# We already know the array strictly decreases from the peak element to the last element.
# We can use a feasible function of arr[i]> arr[i+1] to return true for elements from the peak to the last element.
# Then we realize that it also returns false from the first element to the peak element. We got our feasible function.

# A minor edge case is for the last element as it has no next element.
# We can pad the array with an imaginary node of negative infinity.
# In the implementation, we don't actually need to pad the array as that would incur O(n) extra cost.
# We can just check if i+1 is out of bounds and return true if it is since this implies arr[i] is the last element.

# Now the problem is reduced to finding the first true element in a boolean array.
from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    stat, end = 0, len(arr) - 1

    while stat <= end:
        mid = (stat + end) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            # the peak is found
            return mid
        if arr[mid] >= arr[mid - 1] and arr[mid] < arr[mid + 1]:
            # peak is ahead
            stat = mid + 1
        if arr[mid] <= arr[mid - 1] and arr[mid] > arr[mid + 1]:
            # peak is behind
            end = mid - 1
    return 0


def peak_of_mountain_array_v2(arr: List[int]) -> int:
    length = len(arr)
    left, right = 0, length - 1
    boundary_index = -1

    while left <= right:

        mid = (left + right) // 2

        if mid == length - 1 or arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # res = peak_of_mountain_array(arr)
    # print(res)

    #print(peak_of_mountain_array([0, 1, 2, 3, 2, 1, 0]))
    #print(peak_of_mountain_array([1, 2, 3, 4, 5, 3, 1]))
    #print(peak_of_mountain_array([1, 2, 5, 4, 3, 2, 1, 0]))
    print(peak_of_mountain_array([0, 10, 3, 2, 1, 0]))
