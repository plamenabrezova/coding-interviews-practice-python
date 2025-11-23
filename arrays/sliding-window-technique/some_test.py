def max_len_str(s):
    start = 0
    end = 0
    seen = {}
    max_len = 0

    while end < len(s):
        if s[end] not in seen or seen[s[end]] == False:
            seen[s[end]] = True
            max_len = max(max_len, end - start + 1)

        else:
            while s[start] != s[end]:
                seen[s[start]] = False
                start += 1
            start += 1

        end += 1

    return max_len

print(max_len_str("tmmzuxt"))


s1 = 'plambi'
s2 = 'abc'
lst = list(s2)
lst2 = list(s1)


# for item in lst2:
#     if item in lst:
#         print('yes')

print(all(item in lst2 for item in lst))