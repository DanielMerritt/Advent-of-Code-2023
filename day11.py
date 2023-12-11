def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def get_distance_between_coords(
    coord1: tuple[int, int],
    coord2: tuple[int, int],
    empty_rows: list[int],
    empty_cols: list[int],
    expand: int = 2,
) -> int:
    distance = 0
    for row_idx in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0])):
        if row_idx in empty_rows:
            distance += expand
        else:
            distance += 1
    for col_idx in range(min(coord1[1], coord2[1]), max(coord1[1], coord2[1])):
        if col_idx in empty_cols:
            distance += expand
        else:
            distance += 1
    return distance


def solve(parsed_input: list[str], part=1) -> int:
    grid = [list(line) for line in parsed_input]
    empty_rows = [
        row_idx
        for row_idx in range(len(grid))
        if all(char == "." for char in grid[row_idx])
    ]
    empty_cols = [
        col_idx
        for col_idx in range(len(grid[0]))
        if all(grid[row_idx][col_idx] == "." for row_idx in range(len(grid)))
    ]
    hash_coords: set[tuple[int, int]] = set()
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == "#":
                hash_coords.add((row_idx, col_idx))
    total = 0
    if part == 1:
        expand = 2
    else:
        expand = 1000000
    for coord1 in hash_coords:
        for coord2 in hash_coords:
            total += get_distance_between_coords(
                coord1, coord2, empty_rows, empty_cols, expand=expand
            )
    return total // 2


def main() -> None:
    input_file = "Day11_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
