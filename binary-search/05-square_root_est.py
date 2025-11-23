# Given an integer, find its square root without using the built-in square root function.
# Only return the integer part (truncate the decimals).

# Input: 16
# Output: 4

# Input: 8
# Output: 2
# Explanation: square root of 8 is 2.83..., return the integer part, 2

# Because we truncate the decimals, the problem is equivalent to finding the largest element in the sorted array
# whose square is equal to or less than n.
# As we go from the left to the right of the sorted array, the square of the value increases monotonically.
# We can apply a feasible function of i^2 >=n and yet again reduce this problem to Find the First True in a Sorted
# Boolean Array.
# There is a small caveat: if there is no element in the array whose square equals n,
# then we want to return the largest element that is smaller than the square root of n.
# In this case, we are actually looking for the last false.
# We can subtract 1 from the index after we find the first true from binary search.


def square_root(n: int) -> int:
    lst = []
    result = -1

    for i in range(n + 1):
        lst.append(i)
    start, end = 0, len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] * lst[mid] > n:
            end = mid - 1
        else:
            result = lst[mid]
            start = mid + 1
    return result


def square_root_answer(n: int) -> int:
    if n == 0:
        return 0

    left, right = 1, n
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid

        elif mid * mid > n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result - 1


if __name__ == '__main__':
    # n = int(input())
    # res = square_root(n)
    # print(res)

    print(square_root(10))
    print(square_root(1))
    print(square_root(0))
