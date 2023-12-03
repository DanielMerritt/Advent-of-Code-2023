import re
import string
from typing import Match


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def check_surrounding_coords(
    number_match: Match[str], line_idx: int, parsed_input: list[str]
) -> bool:
    for row_idx in range(line_idx - 1, line_idx + 2):
        for column_idx in range(number_match.start() - 1, number_match.end() + 1):
            try:
                char = parsed_input[row_idx][column_idx]
            except IndexError:
                continue
            if char in string.punctuation and char != ".":
                return True
    return False


def part1(parsed_input: list[str]) -> int:
    total = 0
    for line_idx, line in enumerate(parsed_input):
        number_matches = re.finditer(r"\d+", line)
        for number_match in number_matches:
            if check_surrounding_coords(number_match, line_idx, parsed_input):
                total += int(number_match.group(0))
    return total


class Gear:
    def __init__(self, coords: tuple[int, int]) -> None:
        self.coords = coords
        self.adjacent_nums: list[int] = []


def update_gear_adjacent_numbers(
    number_match: Match[str],
    line_idx: int,
    parsed_input: list[str],
    gear_list: list[Gear],
) -> None:
    for row_idx in range(line_idx - 1, line_idx + 2):
        for column_idx in range(number_match.start() - 1, number_match.end() + 1):
            try:
                char = parsed_input[row_idx][column_idx]
            except IndexError:
                continue
            if char == "*":
                for gear in gear_list:
                    if gear.coords == (row_idx, column_idx):
                        gear.adjacent_nums.append(int(number_match.group(0)))
                        break
                else:
                    gear = Gear((row_idx, column_idx))
                    gear.adjacent_nums.append(int(number_match.group(0)))
                    gear_list.append(gear)


def part2(parsed_input: list[str]) -> int:
    total = 0
    gear_list: list[Gear] = []
    for line_idx, line in enumerate(parsed_input):
        number_matches = re.finditer(r"\d+", line)
        for number_match in number_matches:
            update_gear_adjacent_numbers(
                number_match, line_idx, parsed_input, gear_list
            )
    for gear in gear_list:
        if len(gear.adjacent_nums) == 2:
            total += gear.adjacent_nums[0] * gear.adjacent_nums[1]
    return total


def main() -> None:
    input_file = "Day3_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
