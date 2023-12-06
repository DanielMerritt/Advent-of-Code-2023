from math import floor, ceil


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def get_number_of_winning_possibilities(race: tuple[int, int]) -> int:
    """Use the Quadratic Equation to find the number of winning possibilities via roots"""
    a = -1
    b = race[0]
    c = -race[1]
    first_root = abs((-b + (b**2 - 4 * a * c) ** 0.5) / (-2 * a))
    second_root = abs((-b - (b**2 - 4 * a * c) ** 0.5) / (-2 * a))
    # If roots are ints then remove the tied races
    if first_root == int(first_root):
        first_root += 1
    if second_root == int(second_root):
        second_root -= 1
    return floor(second_root) - ceil(first_root) + 1


def part1(parsed_input: list[str]) -> int:
    times = parsed_input[0].split("Time:")[1].strip().split()
    distances = parsed_input[1].split("Distance:")[1].strip().split()
    races = [(int(time), int(distance)) for time, distance in zip(times, distances)]
    total = 1
    for race in races:
        total *= get_number_of_winning_possibilities(race)
    return total


def part2(parsed_input: list[str]) -> int:
    time = int("".join(parsed_input[0].split("Time:")[1].strip().split()))
    distance = int("".join(parsed_input[1].split("Distance:")[1].strip().split()))
    return get_number_of_winning_possibilities((time, distance))


def main() -> None:
    input_file = "Day6_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
