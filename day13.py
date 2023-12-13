def parse_input(input_file: str) -> list[list[str]]:
    with open(input_file) as f:
        mirrors = f.read().split("\n\n")
        return [mirror.split() for mirror in mirrors]


def get_index(mirror: list[str], target_number_of_differences: int) -> int:
    mirror_index = -1
    for reflection_idx in range(len(mirror[:-1])):
        number_of_differences = 0
        for distance_from_reflection in range(len(mirror)):
            top_idx = reflection_idx - distance_from_reflection
            bottom_idx = reflection_idx + distance_from_reflection + 1
            if top_idx < 0 or bottom_idx >= len(mirror):
                if number_of_differences == target_number_of_differences:
                    mirror_index = reflection_idx
                break
            number_of_differences += sum(
                i != j for i, j in zip(mirror[top_idx], mirror[bottom_idx])
            )
        if mirror_index != -1:
            break
    return mirror_index


def solve(parsed_input: list[list[str]], part=1) -> int:
    if part == 1:
        number_of_differences = 0
    else:
        number_of_differences = 1
    total = 0
    for mirror in parsed_input:
        horizontal_index = get_index(mirror, number_of_differences)
        if horizontal_index != -1:
            total += (horizontal_index + 1) * 100
        rotated_mirror = list(zip(*mirror))
        vertical_index = get_index(rotated_mirror, number_of_differences)
        if vertical_index != -1:
            total += vertical_index + 1
    return total


def main() -> None:
    input_file = "Day13_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
