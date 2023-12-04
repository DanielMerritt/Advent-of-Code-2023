import re


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(parsed_input: list[str]) -> int:
    total = 0
    for card in parsed_input:
        winning_nums, my_nums = re.findall(r"^Card +\d+: ([\d ]+?) \| ([\d ]+)$", card)[
            0
        ]
        winning_nums_set = set(winning_nums.split())
        my_nums_set = set(my_nums.split())
        matches = len(winning_nums_set.intersection(my_nums_set))
        if not matches:
            points = 0
        else:
            points = 2 ** (matches - 1)
        total += points
    return total


def part2(parsed_input: list[str]) -> int:
    last_card = int(re.findall(r"Card +(\d+):", parsed_input[-1])[0])
    card_map = {i: 1 for i in range(1, last_card + 1)}
    for card in parsed_input:
        current_card, winning_nums, my_nums = re.findall(
            r"^Card +(\d+): ([\d ]+?) \| ([\d ]+)$", card
        )[0]
        winning_nums_set = set(winning_nums.split())
        my_nums_set = set(my_nums.split())
        int_current_card = int(current_card)
        matches = len(winning_nums_set.intersection(my_nums_set))
        for card_number in range(int_current_card + 1, int_current_card + matches + 1):
            if card_number > last_card:
                break
            card_map[card_number] += card_map[int_current_card]

    return sum(card_map.values())


def main() -> None:
    input_file = "Day4_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
