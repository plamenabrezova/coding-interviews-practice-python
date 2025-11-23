def find_max_length_distinct_substring(s):
    sliding_window = {}
    # storing the sliding window boundaries
    low = high = 0

    # substring boundaries
    start = end = 0

    if len(s) == 0:
        return 0

    while high < len(s):
        if sliding_window.get(s[high]):
            while s[low] != s[high]:
                sliding_window[s[low]] = False
                low += 1
            low += 1
        else:
            sliding_window[s[high]] = True
            if end - start < high - low:
                start = low
                end = high
        high += 1

    return len(s[start: end + 1])

print(find_max_length_distinct_substring("nfpdmpi"))

