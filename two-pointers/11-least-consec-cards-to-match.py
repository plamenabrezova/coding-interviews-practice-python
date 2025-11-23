# A bunch of cards is laid out in front of you in a line, where the value of each card ranges from 0 to 10^6.
# A pair of cards are matching if they have the same number value.
# Given a list of integer cards, your goal is to match a pair of cards, but you can only pick up cards in a consecutive
# manner. What's the minimum number of cards that you need to pick up to make a pair? If there is no matching pairs,
# return -1.
# For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s
# and picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match a pair of 3s and 4 consecutive cards
# to match 4s, so you need to pick up at least 4 cards to make a match.

from typing import List

def least_consecutive_cards_to_match(cards: List[int]) -> int:
    cards_dict = dict()
    result = float('inf')
    for i in range(len(cards)):
        if cards[i] not in cards_dict:
            cards_dict[cards[i]] = i
        else:
            result = min(result, i - cards_dict[cards[i]] + 1)

    return result if result != float('inf') else -1


if __name__ == '__main__':
    print(least_consecutive_cards_to_match([3, 4, 2, 3, 4, 7]))
