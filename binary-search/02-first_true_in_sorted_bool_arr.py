# An array of boolean values is divided into two sections;
# the left section consists of all false and the right section consists of all true.
# Find the First True in a Sorted Boolean Array of the right section, i.e. the index of the first true element.
# If there is no true element, return -1.
#
# Input: arr = [false, false, true, true, true]
# Output: 2
# Explanation: first true's index is 2.

from typing import List


def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid]:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result

if __name__ == '__main__':
    #arr = [x == "true" for x in input().split()]
    #res = find_boundary(arr)
    #print(res)
    print(find_boundary([False, False, False, False, True]))
    print(find_boundary([False, True, True, True, True, True, True]))
