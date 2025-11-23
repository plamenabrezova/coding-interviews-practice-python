# There is a long table with a line of plates and candles arranged on top of it.
# You are given a 0-indexed string s consisting of characters '*' and '|' only,
# where a '*' represents a plate and a '|' represents a candle.
# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring
# s[lefti...righti] (inclusive).
# For each query, you need to find the number of plates between candles that are in the substring.
# A plate is considered between candles if there is at least one candle to its left and at least one candle to its
# right in the substring.

# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|".
# The number of plates between candles in this substring is 2 (at indices 6 and 7),
# as each of the two plates has at least one candle in the substring to its left and right.
# Return an integer array answer where answer[i] is the answer to the ith query.
#
# Example 1:
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# queries[0] has two plates between candles.
# queries[1] has three plates between candles.

# Example 2
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# queries[0] has nine plates between candles.
# The other queries have zero plates between candles.
# Explanations:
# 1. the index left_pos in candles of the first candle that is greater than qleft means that
# whenever candles[index] >= qleft, we can update left_pos until we find the leftmost index
# candles[index] >= qleft (recurse on left-half).
# 2. the index right_pos in candles of the last candle that is smaller than qright means that
# whenever candles[index] <= qright, we can update right_pos until we find the rightmost index
# candles[index] >= qright (recurse on right-half).
#
# To find the number of plates for each query (qleft, qright), we set up an array candles to store the candles' indices,
# so that we could later do basic arithmetic on the indices to find the number of plates.
# First, we need to find the outside candles' indices in the input s, this can be done via binary search in candles.
# We will find left_pos and right_pos indicating the outside candle's position in s.
# Then, We know that the number of plates is given by the interval between the two bounding candles subtracted by
# the number of candles in between. With the indices left_pos and right_pos,
# we can derive the number of plates to be (candles[right_pos] - candles[left_pos]) - (right_pos - left_pos).

# https://leetcode.com/problems/plates-between-candles/

def plates_btw_candles(s, queries):
    candles = []

    for i in range(len(s)):
        if s[i] == '|':
            candles.append(i)

    result = []
    for q_left, q_right in queries:
        print(q_left)
        print(q_right)
        left_position, right_position = -1, -1

        left, right = 0, len(candles) - 1
        while left <= right:
            mid = (left + right) // 2

            if candles[mid] >= q_left:
                right = mid - 1
                left_position = mid
            else:
                left = mid + 1

        left, right = 0, len(candles) - 1
        while left <= right:
            mid = (left + right) // 2

            if candles[mid] <= q_right:
                left = mid + 1
                right_position = mid
            else:
                right = mid - 1

        if left_position != -1 and right_position != -1 and right_position > left_position:
            result.append((candles[right_position] - candles[left_position]) - (right_position - left_position))
        else:
            result.append(0)
    return result


print(plates_btw_candles('||**||**|*', [[3, 8]]))
