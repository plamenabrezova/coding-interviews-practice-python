def find_longest_substring_with_distinct_chars(string: str):
    # dictionary to keep track of chars present in the current window
    sliding_window = {}

    # storing the sliding window boundaries
    low = high = 0

    # storing the longest substring boundaries
    begin = end = 0

    while high < len(string):
        # check if the current char is present in the current sliding window

        # if the current char is present in the current sliding window remove it
        if sliding_window.get(string[high]):
            # remove chars from the left side of the sliding window
            # until we encounter current char
            while string[low] != string[high]:
                sliding_window[string[low]] = False
                low += 1
            # remove the current char
            low += 1

        # if the current char is not present in the current sliding window include it
        else:
            sliding_window[string[high]] = True

            # if necessary, update the maximum window size
            if end - begin < high - low:
                begin = low
                end = high
        high += 1

    return string[begin:end + 1]


s = 'abbcdafeegh'
print(find_longest_substring_with_distinct_chars(s))