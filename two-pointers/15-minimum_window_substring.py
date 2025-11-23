from collections import defaultdict, Counter

def get_minimum_window(original: str, check: str) -> str:
    m, n = len(original), len(check)

    if m < n:
        return ""

    def is_smaller(w1, w2):  # is w1 smaller than w2
        if w1[1] - w1[0] == w2[1] - w2[0]:
            for i in range(w1[1] - w1[0]):
                if original[w1[0] + i] != original[w2[0] + i]:
                    return original[w1[0] + i] < original[w2[0] + i]
            return False
        else:
            return w1[1] - w1[0] < w2[1] - w2[0]

    # counter for different characters and their count in check string
    check_count = Counter(check)
    # counter for different characters and their count in window
    window_count = defaultdict(int)

    # number of required symbols depending on the length of the check string
    required = len(check_count.keys())
    # number of satisfied symbols in the window - starting from zero
    satisfied = 0

    # initialize "empty" window of size (m+1)
    window = (-m - 1, 0)

    # starting point for the window
    left = 0

    for right in range(m):
        currently_pointed = original[right]

        # keep track only of characters that appear in check
        if currently_pointed in check_count:
            window_count[currently_pointed] += 1
            # if in the window there are enough number of chars that satisfies check
            if window_count[currently_pointed] == check_count[currently_pointed]:
                satisfied += 1

        # try to shrink the window, so that the result is the shortest substring
        while satisfied == required:  # valid window

            if is_smaller((left, right + 1), window):  # new window is smaller than window
                window = (left, right + 1)

            # delete only characters from check
            if original[left] in check_count:
                window_count[original[left]] -= 1

                # removing original[l] makes window dissatisfied
                if window_count[original[left]] < check_count[original[left]]:
                    satisfied -= 1
            left += 1

    return original[window[0]: window[1]]


if __name__ == '__main__':
    print(get_minimum_window('cdbaebaecd', 'abc'))
