def maxSum(arr, n, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        # we swap the first element with the element that will come next in the sequence
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))