def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def get_next_value_in_sequence(sequence: list[int]) -> int:
    if all(i == 0 for i in sequence):
        return 0
    return sequence[-1] + get_next_value_in_sequence(
        [j - i for i, j in zip(sequence, sequence[1:])]
    )


def solve(parsed_input: list[str], part: int = 1) -> int:
    total = 0
    for line in parsed_input:
        values = list(map(int, line.split()))
        if part == 2:
            values.reverse()
        total += get_next_value_in_sequence(values)
    return total


def main() -> None:
    input_file = "Day9_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
