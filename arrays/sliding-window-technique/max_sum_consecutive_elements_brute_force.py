import sys

INT_MIN = -sys.maxsize - 1

def max_sum_func(arr, n, c):
    max_sum = INT_MIN

    for i in range(n - c + 1):
        current_sum = 0
        for j in range(c):
            current_sum = current_sum + arr[i + j]
        max_sum = max(current_sum, max_sum)
    return max_sum

input_array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
elements_count = len(input_array)
consecutive_elements = 4

print(max_sum_func(input_array, elements_count, consecutive_elements))