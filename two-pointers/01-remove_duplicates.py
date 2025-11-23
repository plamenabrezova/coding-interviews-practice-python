from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(arr):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1

    return slow + 1

if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    # res = remove_duplicates(arr)
    # print(' '.join(map(str, arr[:res])))
    print(remove_duplicates([0, 0, 1, 1, 1, 2, 2]))
