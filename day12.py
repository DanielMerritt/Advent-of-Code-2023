from functools import cache


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


@cache
def number_of_arrangements(springs: str, nums: tuple[int, ...]) -> int:
    total = 0
    if len(springs) == 0:
        if len(nums) == 0:
            return 1
        return 0
    elif len(nums) == 0:
        if "#" in springs:
            return 0
        return 1
    elif sum(nums) + len(nums) - 1 > len(springs):
        return 0
    if springs[0] == "?":
        total += number_of_arrangements("#" + springs[1:], nums)
        total += number_of_arrangements("." + springs[1:], nums)
    elif springs[0] == ".":
        total += number_of_arrangements(springs[1:], nums)
    elif springs[0] == "#":
        possible_fit = True
        if not all(spring != "." for spring in springs[: nums[0]]):
            possible_fit = False
        elif len(springs) > nums[0]:
            if springs[nums[0]] == "#":
                possible_fit = False
        if possible_fit:
            total += number_of_arrangements(springs[nums[0] + 1 :], nums[1:])
    return total


def solve(parsed_input: list[str], part: int = 1) -> int:
    total = 0
    for line in parsed_input:
        springs, parsed_nums = line.split()
        nums = tuple(map(int, parsed_nums.split(",")))
        if part == 2:
            unfolded_springs = "?".join([springs] * 5)
            unfolded_nums = nums * 5
            total += number_of_arrangements(unfolded_springs, unfolded_nums)
        else:
            total += number_of_arrangements(springs, nums)
    return total


def main() -> None:
    input_file = "Day12_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
