from sys import maxsize


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def map_number(maps: list[tuple[int, ...]], current_num: int) -> int:
    for number_mapping in maps:
        if (
            current_num >= number_mapping[1]
            and current_num < number_mapping[1] + number_mapping[2]
        ):
            return number_mapping[0] + current_num - number_mapping[1]
    else:
        return current_num


def part1(parsed_input: list[str]) -> int:
    seeds = map(int, parsed_input[0].split("seeds: ")[1].split())
    lowest_num = maxsize
    for seed in seeds:
        current_num = seed
        maps: list[tuple[int, ...]] = []
        for line in parsed_input[3:]:
            if not line:
                current_num = map_number(maps, current_num)
                maps = []
                continue
            if line[0].isdigit():
                maps.append(tuple(map(int, line.split())))
        current_num = map_number(maps, current_num)
        if current_num < lowest_num:
            lowest_num = current_num
    return lowest_num


def apply_transformation(
    range_to_transform: tuple[int, int], number_mapping: tuple[int, ...]
) -> tuple[int, int]:
    start_num = range_to_transform[0] + number_mapping[0] - number_mapping[1]
    end_num = range_to_transform[1] + number_mapping[0] - number_mapping[1]
    return (start_num, end_num)


def map_range(
    maps: list[tuple[int, ...]], current_ranges: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    new_ranges: list[tuple[int, int]] = []
    while current_ranges:
        current_range = current_ranges.pop()
        for number_mapping in maps:
            number_range = (
                number_mapping[1],
                number_mapping[1] + number_mapping[2] - 1,
            )
            if (
                number_range[0] <= current_range[1]
                and number_range[1] >= current_range[0]
            ):
                overlapping_start = max(number_range[0], current_range[0])
                overlapping_end = min(number_range[1], current_range[1])
                new_ranges.append(
                    apply_transformation(
                        (overlapping_start, overlapping_end), number_mapping
                    )
                )
                if current_range[0] < number_range[0]:
                    current_ranges.append((current_range[0], number_range[0] - 1))
                if current_range[1] > number_range[1]:
                    current_ranges.append((number_range[1] + 1, current_range[1]))
                break
        else:
            new_ranges.append(current_range)
    return new_ranges


def part2(parsed_input: list[str]) -> int:
    parsed_seeds = parsed_input[0].split("seeds: ")[1].split()
    current_ranges: list[tuple[int, int]] = [
        (int(parsed_seeds[i]), int(parsed_seeds[i]) + int(parsed_seeds[i + 1]) - 1)
        for i in range(0, len(parsed_seeds), 2)
    ]
    maps: list[tuple[int, ...]] = []
    for line in parsed_input[3:]:
        if not line:
            current_ranges = map_range(maps, current_ranges)
            maps = []
            continue
        if line[0].isdigit():
            maps.append(tuple(map(int, line.split())))
    current_ranges = map_range(maps, current_ranges)
    return min([min(num) for num in current_ranges])


def main() -> None:
    input_file = "Day5_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
