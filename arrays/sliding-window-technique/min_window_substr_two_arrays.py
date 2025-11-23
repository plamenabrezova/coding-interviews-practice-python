from collections import Counter


def check_dup(lst1, lst2):
    lst1_counter = Counter(lst1)
    lst2_counter = Counter(lst2)

    for i in lst2_counter:
        if type(lst1_counter.get(i)) == int and lst2_counter.get(i) > lst1_counter.get(i):
            return False
    return True


def solution(s, t):
    source_list = list(s)
    target_list = list(t)
    result = ""
    if len(t) > len(s) or not all(item in source_list for item in target_list):
        return result

    start = 0
    end = 0
    min_length = float('inf')

    while end < len(s):
        while all(item in source_list[start: end + 1] for item in target_list) and check_dup(source_list[start: end + 1], target_list):
            if end - start + 1 <= min_length:
                result = source_list[start: end + 1]
            min_length = min(min_length, end - start + 1)
            start += 1

        end += 1
    return ''.join(result)


print(solution('ADOBECODEBANC','ABC'))
print(solution('a', 'a'))
print(solution('aa', 'aa'))
print(solution('bbaa','aba'))
