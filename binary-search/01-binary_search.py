# Binary search is an efficient array search algorithm.
# It works by narrowing down the search range by half each time.
# If you have looked up a word in a physical dictionary, you've already used binary search in real life.
#
# Given a sorted array of integers and an integer called target,
# find the element that equals the target and return its index.
# If the element is not found, return -1.
#
# The key observation here is that the array is sorted.
# We pick a random element in the array and compare it to the target.
#
# If we happen to pick the element that equals the target (how lucky!), then bingo. We return its index.
# If the element is smaller than the target, then we know the target cannot be found in the section to the left
# of the current element since everything to the left is even smaller.
# So we discard the current element and everything on the left from the search range.
# If the element is larger than the target, then we know the target cannot be found in the section to the right
# of the current element since everything to the right is even larger.
# So we discard the current element and everything on the right from the search range.

# We repeat this process until we find the target.
# Instead of picking a random element, we always pick the middle element in the current search range.
# This way, we can discard half of the options and shrink the search range by half each time.
# This gives us O(log(N)) runtime.


def binary_search(arr, target) -> int:
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

print(binary_search([1, 3, 5, 7, 8], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 0))
print(binary_search([2, 8, 89, 120, 1000], 120))
print(binary_search([1, 2, 3, 4, 5], 10))