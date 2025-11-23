def solution(s: str, t: str) -> str:
    target = {}
    for char in t:
        if char not in target:
            target[char] = 0
        target[char] += 1
    print(target)

    count_remaining_chars = sum(target.values())
    min_length = len(s)
    start = 0
    end = 0

    found_flag = False
    left = 0
    right = 0

    while end < len(s):
        if s[end] in target:
            target[s[end]] -= 1

            if target[s[end]] >= 0:
                count_remaining_chars -= 1

        while count_remaining_chars == 0:
            found_flag = True
            # min_length = min(min_length, end - start + 1)
            if min_length >= end - start + 1:
                min_length = end - start
                left = start
                right = end

            if s[start] in target:
                if target[s[start]] == 0:
                    count_remaining_chars += 1
                    target[s[start]] += 1
                elif target[s[start]] < 0:
                    target[s[start]] += 1

            start += 1

        end += 1

    print(count_remaining_chars)

    # until counter is greater than zero
    return "" if not found_flag else s[left: right + 1]

#print(solution('palkmi', 'pl'))
print(solution('ADOBECODEBANC', 'ABC'))
print(solution('aa', 'aa'))