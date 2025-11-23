def find_max_length_distinct_substring(input_string):
    sliding_window = {}
    # storing the sliding window boundaries
    low = high = 0
    # substring boundaries
    start = end = 0

    if len(input_string) == 0:
        return 0

    while high < len(input_string):
        if sliding_window.get(input_string[high]):
            while input_string[low] != input_string[high]:
                sliding_window[input_string[low]] = False
                low += 1
            low += 1
        else:
            sliding_window[input_string[high]] = True
            if end - start < high - low:
                start = low
                end = high
        high += 1

    return len(input_string[start: end + 1])

print(find_max_length_distinct_substring("nfpdmpi"))

