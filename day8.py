from itertools import cycle
from typing import Iterator
import re
from math import lcm


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(instruction_map: dict[str, tuple[str, str]], instructions: Iterator) -> int:
    current_location = "AAA"
    if current_location not in instruction_map:
        return 0
    count = 0
    for count, instruction in enumerate(instructions, start=1):
        if instruction == "R":
            current_location = instruction_map[current_location][1]
        elif instruction == "L":
            current_location = instruction_map[current_location][0]
        if current_location == "ZZZ":
            break
    return count


def get_cycle_size(
    starting_location: str,
    instruction_map: dict[str, tuple[str, str]],
    instructions: Iterator,
) -> int:
    count = 0
    current_location = starting_location
    for count, instruction in enumerate(instructions, start=1):
        if instruction == "R":
            current_location = instruction_map[current_location][1]
        elif instruction == "L":
            current_location = instruction_map[current_location][0]
        if current_location.endswith("Z"):
            break
    return count


def part2(instruction_map: dict[str, tuple[str, str]], instructions: Iterator) -> int:
    current_locations = [
        instruction for instruction in instruction_map if instruction.endswith("A")
    ]
    cycle_sizes = [
        get_cycle_size(current_location, instruction_map, instructions)
        for current_location in current_locations
    ]
    return lcm(*cycle_sizes)


def solve(parsed_input: list[str], part: int = 1) -> int:
    instructions = cycle(parsed_input[0])
    instruction_map: dict[str, tuple[str, str]] = {}
    for line in parsed_input[2:]:
        source, left_dest, right_dest = re.findall(r"[A-Z\d]{3}", line)
        instruction_map[source] = (left_dest, right_dest)
    if part == 1:
        return part1(instruction_map, instructions)
    else:
        return part2(instruction_map, instructions)


def main() -> None:
    input_file = "Day8_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
