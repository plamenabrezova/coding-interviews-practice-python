# Find the length of the longest substring of a given string without repeating characters.
# Input: abccabcabcc
# Output: 3
# Explanation: longest substrings are abc, cab, both of length 3
# Input: aaaabaaa
# Output: 2
# Explanation: ab is the longest substring, length 2

# The template
# def sliding_window_flexible_longest(input):
#     initialize window, ans
#     left = 0
#     for right in range(len(input)):
#         append input[right] to window
#         while invalid(window):        # update left until window is valid again
#             remove input[left] from window
#             left += 1
#         ans = max(ans, window)        # window is guaranteed to be valid here
#     return ans

def longest_substring_without_repeating_characters(s: str) -> int:
    window, result = '', 0
    left = 0
    for right in range(len(s)):
        while s[right] in window:
            window = window[1: right + 1]
            left += 1

        window += s[right]
        result = max(result, len(window))
    return result


if __name__ == '__main__':
    # print(longest_substring_without_repeating_characters('abccabcabcc'))
    print(longest_substring_without_repeating_characters('abcdbea'))
