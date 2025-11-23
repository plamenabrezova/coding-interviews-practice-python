def min_sub_array_len(target, nums_array) -> int:
    if sum(nums_array) < target:
        return 0

    min_length = len(nums_array)

    for start in range(len(nums_array)):
        end = start
        res = nums_array[start]

        while res < target and end < len(nums_array) - 1:
            end += 1
            res += nums_array[end]

        if res >= target:
            if start == end:
                min_length = 1
            else:
                min_length = min(min_length, end - start + 1)

    return min_length

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

def min_sub_sum(target, nums_array):
    res = sum(nums_array)
    if res < target:
        return 0
    start = 0
    end = len(nums_array) - 1
    min_length = len(nums_array)
    n = nums_array

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

#input_nums_array = [12,28,83,4,25,26,25,2,25,25,25,12]
#input_nums_array = [5,1,3,5,10,7,4,9,2,8]
#input_nums_array = [1,1,1,1,7]
#input_nums_array = [1,2,3,4,5]
input_nums_array = [2, 3, 1, 2, 4, 3]
for r in enumerate(input_nums_array):
    print(r)

print(min_sub_array_len(7, input_nums_array))
print(min_sub_sum(7, input_nums_array))
#print(min_sub_sum(15, input_nums_array))
#print(min_sub_sum(7, input_nums_array))

#print(input_nums_array.index(max(input_nums_array)))
#print(input_nums_array[0:input_nums_array.index(max(input_nums_array))] + input_nums_array[input_nums_array.index(max(input_nums_array)):-1])
#print(min_sub_array_len(11, input_nums_array))

# def min_sub(target, nums_array):
#     if sum(nums_array) < target:
#         return 0
#
#     min_length = len(nums_array)
#     res = 0
#     idx = 0
#     n = nums_array
#     while res < target:
#         res += max(n)
#         idx += 1
#         n = n[0:n.index(max(n))] + n[n.index(max(n)):-1]
#
#     min_length = idx
#     return min_length

# input_nums_array = [1,2,3,4,5]
# print(min_sub(11, input_nums_array))