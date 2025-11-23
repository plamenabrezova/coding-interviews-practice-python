# Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case.

# Input: Do geese see God? Output: True
# Input: Was it a car or a cat I saw? Output: True
# Input: A brown fox jumping over Output: False
import string

def is_palindrome(s: str) -> bool:
    s = ''.join([char for char in s.lower() if char.isalpha()])
    # list
    # s = [char for char in s.lower() if char.isalpha()]
    p2 = len(s) - 1

    for p1 in range(len(s)):
        if s[p1] == s[p2]:
            p2 -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    # s = input()
    # res = is_palindrome(s)
    # print('true' if res else 'false')
    print(is_palindrome('Do geese see God?'))