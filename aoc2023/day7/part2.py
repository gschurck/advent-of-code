import enum
import itertools
from collections import Counter, OrderedDict, defaultdict
from enum import Enum

from aoc import get_input

result = 0
ranked_hands = []
hands_by_type = defaultdict(list)
total_winnings = 0


class HandType(enum.IntEnum):
    FIVEOFAKIND = 1
    FOUROFAKIND = 2
    FULLHOUSE = 3
    THREEOFAKIND = 4
    TWOPAIR = 5
    ONEPAIR = 6
    HIGHCARD = 7


for line in get_input():
    line = line.strip("\n")
    hand, bid = line.split()
    bid = int(bid)
    print(hand)

    cards_counts_dict = Counter(hand)
    jokers = cards_counts_dict.pop('J', 0)
    print(cards_counts_dict)
    cards_counts = sorted(cards_counts_dict.values(), reverse=True)
    print(cards_counts)
    card_type = None
    max_cards = cards_counts[0] + jokers if len(cards_counts) else jokers
    if max_cards == 5:
        card_type = HandType.FIVEOFAKIND
    elif max_cards == 4:
        card_type = HandType.FOUROFAKIND
    elif max_cards == 3 and cards_counts[1] == 2:
        card_type = HandType.FULLHOUSE
    elif max_cards == 3 and cards_counts[1] == 1:
        card_type = HandType.THREEOFAKIND
    elif max_cards == 2 and cards_counts[1] == 2:
        card_type = HandType.TWOPAIR
    elif max_cards == 2 and cards_counts[1] == 1:
        card_type = HandType.ONEPAIR
    elif max_cards == 1:
        card_type = HandType.HIGHCARD
    print(card_type)
    hands_by_type[card_type].append((hand, bid, card_type))

cards_order = "AKQT98765432J"[::-1]
print(hands_by_type)
for hands_with_type in hands_by_type.items():
    hands_with_type_key, hands_with_type_list = hands_with_type
    if len(hands_by_type) < 2:
        continue
    hands_by_type[hands_with_type_key] = sorted(hands_with_type_list,
                                                key=lambda hand: [cards_order.index(card[0]) for card in hand[0]])
print(hands_by_type)
hands_by_type = dict(sorted(hands_by_type.items(), reverse=True))
print(hands_by_type)
print(hands_by_type.values())
ranked_hands = list(itertools.chain.from_iterable(hands_by_type.values()))

for id_hand, ranked_hand in enumerate(ranked_hands):
    rank = id_hand + 1
    print(f"adding {ranked_hand[1]} * {rank}")
    result += ranked_hand[1] * rank
print(result)
