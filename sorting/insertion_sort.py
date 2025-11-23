from typing import List

def insertion_sort(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

if __name__ == '__main__':
    result = insertion_sort([3, 5, 18, 1, 32, 19, 87, 4])
    print(' '.join(map(str, result)))