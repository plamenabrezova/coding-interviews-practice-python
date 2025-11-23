# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def max_profit(prices) -> int:
    # buy
    left = 0
    # sell
    right = 1

    profit = 0

    while right < len(prices):
        left_value = prices[left]
        right_value = prices[right]

        if left_value > right_value:
            left = right
        else:
            profit = profit + (right_value - left_value)
            left = right

        right += 1

    return profit

print(max_profit([7,1,5,3,6,4]))