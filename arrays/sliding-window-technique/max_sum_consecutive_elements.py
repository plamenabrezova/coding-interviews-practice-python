def max_sum_func(arr, n, c):
    window_sum = sum(arr[:c])
    max_sum = window_sum

    for i in range(n - c):
        # we swap the first element with the element that will come next in the sequence
        window_sum = window_sum - arr[i] + arr[i + c]
        max_sum = max(window_sum, max_sum)

    return max_sum

input_arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
elements_count = len(input_arr)
consecutive_elements = 4
print(max_sum_func(input_arr, elements_count, consecutive_elements))