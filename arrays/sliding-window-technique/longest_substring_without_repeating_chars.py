def length_of_longest_substring(input_str: str) -> int:
    length = len(input_str)
    result = 0

    for start in range(length):
        visited = [0] * 256
        for end in range(start, length):
            if visited[ord(input_str[end])]:
                break
            else:
                result = max(result, end - start + 1)
                visited[ord(input_str[end])] = True
        visited[ord(input_str[start])] = False

    return result

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"
# s = 'pwwkew'
#s = 'aab'
print(length_of_longest_substring(s))