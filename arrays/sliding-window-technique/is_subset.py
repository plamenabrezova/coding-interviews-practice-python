from collections import Counter


def is_subset(A: list[str], B: list[str]) -> bool:
    """is_subset tests if all elements of A
    are included in B.

    Args:
        A (list[str]): List of string elements.
        B (list[str]): List of string elements.

    Returns:
        bool: True if all elements of A (inc. duplicates) are in B.
    """
    # Create counter objs
    c_A = Counter(A)
    c_B = Counter(B)
    # First check to make sure unique elements are a subset
    # Or it fails at this stage
    uniq_A = c_A.keys()
    uniq_B = c_B.keys()
    if uniq_A <= uniq_B:
        if c_B != c_A:
            return bool(c_B - c_A)
        return True
        # return bool(c_B - c_A) if c_B != c_A else True
    return False


if __name__ == '__main__':
    s = ["A", "A", "b", "b"]
    t = ["A", "A", "b", "b", "b"]
    k = ["A", "b", "z"]

    print(is_subset(t, t))  # True
    print(is_subset(k, s))  # False
    print(is_subset(s, t))  # True