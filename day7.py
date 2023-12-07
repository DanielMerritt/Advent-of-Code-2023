from collections import Counter


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def get_hand_values(hand: str, jack_value: int = 11) -> list[int]:
    hand_value_dict = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": jack_value,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    hand_value_list = [hand_value_dict[card_value] for card_value in hand]
    return hand_value_list


def get_hand_type(hand: str) -> int:
    type_counts = Counter(hand)
    # Five of a kind
    if max(type_counts.values()) == 5:
        return 7
    # Four of a kind
    elif max(type_counts.values()) == 4:
        return 6
    # Full House
    elif 3 in type_counts.values() and 2 in type_counts.values():
        return 5
    # Three of a kind
    elif max(type_counts.values()) == 3:
        return 4
    # Two pair
    elif list(type_counts.values()).count(2) == 2:
        return 3
    # One pair
    elif max(type_counts.values()) == 2:
        return 2
    # High card
    else:
        return 1


def get_hand_type_with_jokers(hand: str) -> int:
    hand_type = 1
    for joker_possiblity in list(map(str, range(2, 10))) + ["T", "Q", "K", "A"]:
        temp_hand = hand.replace("J", joker_possiblity)
        temp_hand_type = get_hand_type(temp_hand)
        if temp_hand_type > hand_type:
            hand_type = temp_hand_type
    return hand_type


def solve(parsed_input: list[str], part: int = 1) -> int:
    data: list[tuple[str, int]] = []
    for line in parsed_input:
        hand, bid = line.split()
        data.append((hand, int(bid)))
    if part == 1:
        sorted_data = sorted(
            data, key=lambda x: (get_hand_type(x[0]), get_hand_values(x[0]))
        )
    else:
        sorted_data = sorted(
            data,
            key=lambda x: (
                get_hand_type_with_jokers(x[0]),
                get_hand_values(x[0], jack_value=1),
            ),
        )
    total = 0
    rank = 1
    for _, value in sorted_data:
        total += rank * value
        rank += 1
    return total


def main() -> None:
    input_file = "Day7_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
