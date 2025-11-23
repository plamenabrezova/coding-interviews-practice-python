from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    for i in range(len(unsorted_list)):
        for k in range(i + 1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[k]:
                (unsorted_list[i], unsorted_list[k]) = (unsorted_list[k], unsorted_list[i])

    return unsorted_list

def sort_list_insertion_sort(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list


if __name__ == '__main__':
    # unsorted_list = [int(x) for x in input().split()]
    # res = sort_list(unsorted_list)
    # print(' '.join(map(str, res)))

    print(sort_list([5, 3, 1, 2, 4]))
