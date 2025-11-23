# Given a string original and a string check, find the starting index of all substrings of original that is
# an anagram of check. The output must be sorted in ascending order.

# Parameters
# original: A string
# check: A string
# Result
# A list of integers representing the starting indices of all anagrams of check.

# Example 1
# Input: original = "cbaebabacd", check = "abc"
# Output: [0, 6]
# Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".

# Example 2
# Input: original = "abab", check = "ab"
# Output: [0, 1, 2]
# Explanation: All substrings with length 2 from "abab" is an anagram of "ab".

from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    original_len, check_len = len(original), len(check)
    if original_len < check_len:
        return []
    result = []

    # stores the frequency of each character in the check string
    check_counter = [0] * 26
    # stores the frequency of each character in the current window
    window = [0] * 26

    a = ord('a')  # ascii value of 'a'

    # first window
    for i in range(check_len):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1

    if window == check_counter:
        result.append(0)

    for i in range(check_len, original_len):
        window[ord(original[i - check_len]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            result.append(i - check_len + 1)

    return result


if __name__ == '__main__':
    # original = input()
    # check = input()
    # res = find_all_anagrams(original, check)
    # print(' '.join(map(str, res)))
    print(find_all_anagrams('cbaebabacd', 'abc'))
    test = ['a', 'b', 'c']
    test1 = ['c', 'b', 'a']
    print(test)
