def length_of_longest_substring(input_str: str) -> int:
    chars_seen = {}
    max_length = 0
    start = 0

    for end in range(len(input_str)):
        if input_str[end] in chars_seen and chars_seen[input_str[end]] >= start:
            start = chars_seen[input_str[end]] + 1
        chars_seen[input_str[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

#s = "abcabcbb"
s = 'pwwkew'
#s = 'aab'
print(length_of_longest_substring(s))