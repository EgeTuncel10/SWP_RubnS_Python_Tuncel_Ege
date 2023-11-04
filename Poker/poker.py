import json
import math
import random

# floor-division ... color
# modulo ... number


def init():
    poker_cards = []
    for a in range(52):
        poker_cards.append(a)

    return poker_cards


def draw_five_cards(poker_cards, amount_of_cards):
    return random.sample(poker_cards, k=amount_of_cards)


combinations = {"Royal Flush": 0, "Straight Flush": 0, "Four of a Kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "Three of a Kind": 0, "Two Pair": 0, "One Pair": 0, "High Card": 0}


def capture_combinations(hand):
    if royal_flush(hand):
        combinations["Royal Flush"] += 1
        return
    if straight_flush(hand):
        combinations["Straight Flush"] += 1
        return
    if four_of_a_kind(hand):
        combinations["Four of a Kind"] += 1
        return
    if full_house(hand):
        combinations["Full House"] += 1
        return
    if flush(hand):
        combinations["Flush"] += 1
        return
    if straight(hand):
        combinations["Straight"] += 1
        return
    if three_of_a_kind(hand):
        combinations["Three of a Kind"] += 1
        return
    if two_pair(hand):
        combinations["Two Pair"] += 1
        return
    if one_pair(hand):
        combinations["One Pair"] += 1
        return
    if high_card():
        combinations["High Card"] += 1
        return


def royal_flush(hand):
    # eigentlich übersetzt dieser den oberen Codeblock --> testen
    # royal_count = sum(1 for card in cards if (card // 13) == (hand[0] // 13)
    #if royal_count >= 5
    if flush(hand):
        numbers_in_a_row = [8, 9, 10, 11, 12]
        for card in hand:
            if (card % 13) in numbers_in_a_row:
                numbers_in_a_row.remove(card % 13)

        if len(numbers_in_a_row) == 0:
            return True
        else:
            return False
    else:
        return False


def straight_flush(hand):
    if flush(hand):
        if straight(hand):
            return True
        else:
            return False
    else:
        return False


def four_of_a_kind(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    for a in range(len(hand)-1):
        for b in range(len(hand)):
            if (numbers_in_a_row[a] % 13) == (numbers_in_a_row[b] % 13) and (a != b):
                count += 1
        if count >= 3:
            return True
        else:
            count = 0

    return False


def full_house(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    cards_to_remove = []
    for a in range(len(numbers_in_a_row) - 1):
        for b in range(len(numbers_in_a_row)):
            if (numbers_in_a_row[a] % 13) == (numbers_in_a_row[b] % 13) and (a != b):
                count += 1
                cards_to_remove.append(numbers_in_a_row[b])
        if count >= 2:
            left_cards = numbers_in_a_row.copy()
            for c in cards_to_remove:
                #if c in left_cards:
                left_cards.remove(c)
            for d in range(len(left_cards) - 1):
                for e in range(len(left_cards)):
                    if ((left_cards[d] % 13) == (left_cards[e] % 13)) and (d != e):
                        return True

            return False
        else:
            count = 0
            cards_to_remove = []
            #numbers_in_a_row = sorted(hand)

    return False


def flush(hand):
    hearts = 0
    diamonds = 0
    clubs = 0
    spades = 0
    for card in hand:
        if 0 == (card // 13):
            hearts += 1
    for card in hand:
        if 1 == (card // 13):
            diamonds += 1
    for card in hand:
        if 2 == (card // 13):
            clubs += 1
    for card in hand:
        if 3 == (card // 13):
            spades += 1

    if (hearts or diamonds or clubs or spades) >= 5:
        return True
    else:
        return False


def straight(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    five_or_ten_in_straight = False
    for a in range(len(hand) - 1):
        if (numbers_in_a_row[a] % 13) == (numbers_in_a_row[a + 1] % 13) - 1:
            count += 1
            if (((numbers_in_a_row[a + 1] % 13)-1) == 4) or (((numbers_in_a_row[a + 1] % 13)-1) == 9):
                five_or_ten_in_straight = True

    if count >= 4 and five_or_ten_in_straight:
        return True
    else:
        return False


def three_of_a_kind(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    for a in range(len(hand) - 1):
        for b in range(len(hand)):
            if (numbers_in_a_row[a] % 13) == (numbers_in_a_row[b] % 13) and (a != b):
                count += 1
        if count >= 2:
            return True
        else:
            count = 0

    return False


def two_pair(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    cards_to_remove = []
    for a in range(len(numbers_in_a_row) - 1):
        for b in range(len(numbers_in_a_row)):
            if ((numbers_in_a_row[a] % 13) == (numbers_in_a_row[b] % 13)) and (a != b):
                count += 1
                cards_to_remove.append(numbers_in_a_row[b])
                cards_to_remove.append(numbers_in_a_row[a])
        if count >= 1:
            left_cards = numbers_in_a_row.copy()
            for c in cards_to_remove:
                left_cards.remove(c)
            count = 0
            for d in range(len(left_cards) - 1):
                for e in range(len(left_cards)):
                    if ((left_cards[d] % 13) == (left_cards[e] % 13)) and (d != e):
                        count += 1
                if count >= 1:
                    return True
                else:
                    count = 0
                    cards_to_remove = []
        else:
            count = 0
            cards_to_remove = []

    return False


def one_pair(hand):
    numbers_in_a_row = sorted(hand)
    count = 0
    for a in range(len(hand) - 1):
        for b in range(len(hand)):
            if ((numbers_in_a_row[a] % 13) == (numbers_in_a_row[b] % 13)) and (a != b):
                count += 1
        if count >= 1:
            return True
        else:
            count = 0

    return False


def high_card():
    return True


if __name__ == '__main__':
    drawings = 1000000
    for i in range(drawings):
        capture_combinations(draw_five_cards(init(), 5))

    count = combinations["Royal Flush"] + combinations["Straight Flush"] + combinations["Four of a Kind"] + \
            combinations["Full House"] + combinations["Flush"] + combinations["Straight"] + combinations[
                "Three of a Kind"] + combinations["Two Pair"] + combinations["One Pair"] + combinations["High Card"]

    print(json.dumps(combinations, indent=4))
    print("Amount of drawing: " + str(count))

    statistics = {
        "Royal Flush": (combinations["Royal Flush"]/drawings)*100,
        "Straight Flush": (combinations["Straight Flush"]/drawings)*100,
        "Four of a Kind": (combinations["Four of a Kind"]/drawings)*100,
        "Full House": (combinations["Full House"]/drawings)*100,
        "Flush": (combinations["Flush"]/drawings)*100,
        "Straight": (combinations["Straight"]/drawings)*100,
        "Three of a Kind": (combinations["Three of a Kind"]/drawings)*100,
        "Two Pair": (combinations["Two Pair"]/drawings)*100,
        "One Pair": (combinations["One Pair"]/drawings)*100,
        "High Card": (combinations["High Card"]/drawings)*100
    }
    print(json.dumps(statistics, indent=4))


