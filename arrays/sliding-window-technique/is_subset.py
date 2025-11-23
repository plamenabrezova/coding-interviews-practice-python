# The goal is to check is all elements in one array are included in another array .
# Return true if all elements of first array(inc. duplicates) are in present in the second array.

from collections import Counter

def is_subset(first_array: list[str], second_array: list[str]) -> bool:
    counter_first_array = Counter(first_array)
    counter_second_array = Counter(second_array)

    # check if unique elements from both arrays are a subset otherwise fails at this stage
    unique_elements_first_array = counter_first_array.keys()
    unique_elements_second_array = counter_second_array.keys()
    if unique_elements_first_array <= unique_elements_second_array:
        if counter_second_array != counter_first_array:
            return bool(counter_second_array - counter_first_array)
        return True
    return False
    # return bool(counter_second_array - counter_first_array) if counter_second_array != counter_first_array else True


if __name__ == '__main__':
    s = ["A", "A", "b", "b"]
    t = ["A", "A", "b", "b", "b"]
    k = ["A", "b", "z"]

    print(is_subset(t, t))  # True
    print(is_subset(k, s))  # False
    print(is_subset(s, t))  # True