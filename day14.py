from enum import Enum, auto


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


def tilt(grid: list[list[str]], direction: Direction) -> None:
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == "O":
                target_location = (row_idx, col_idx)
                if direction == Direction.NORTH:
                    for i in range(row_idx - 1, -1, -1):
                        if grid[i][col_idx] == ".":
                            target_location = (i, col_idx)
                        elif grid[i][col_idx] == "#":
                            break
                elif direction == Direction.EAST:
                    for i in range(col_idx + 1, len(grid[row_idx])):
                        if grid[row_idx][i] == ".":
                            target_location = (row_idx, i)
                        elif grid[row_idx][i] == "#":
                            break

                elif direction == Direction.SOUTH:
                    for i in range(row_idx + 1, len(grid)):
                        if grid[i][col_idx] == ".":
                            target_location = (i, col_idx)
                        elif grid[i][col_idx] == "#":
                            break

                elif direction == Direction.WEST:
                    for i in range(col_idx - 1, -1, -1):
                        if grid[row_idx][i] == ".":
                            target_location = (row_idx, i)
                        elif grid[row_idx][i] == "#":
                            break

                grid[row_idx][col_idx] = "."
                grid[target_location[0]][target_location[1]] = "O"


def get_load(grid: list[list[str]]) -> int:
    total = 0
    for row_idx in range(len(grid)):
        multiplier = len(grid) - row_idx
        total += sum(1 for char in grid[row_idx] if char == "O") * multiplier
    return total


def part1(parsed_input: list[str]) -> int:
    grid = [list(line) for line in parsed_input]
    tilt(grid, Direction.NORTH)
    load = get_load(grid)
    return load


def cycle_grid(grid: list[list[str]]) -> None:
    tilt(grid, Direction.NORTH)
    tilt(grid, Direction.WEST)
    tilt(grid, Direction.SOUTH)
    tilt(grid, Direction.EAST)


def hash_grid(grid: list[list[str]]) -> int:
    return hash(tuple(map(tuple, grid)))


def part2(parsed_input: list[str]) -> int:
    grid = [list(line) for line in parsed_input]
    hashes = {}
    cycle_num = 1
    while True:
        cycle_grid(grid)
        grid_hash = hash_grid(grid)
        if grid_hash in hashes:
            loop_start = hashes[grid_hash]
            loop_end = cycle_num
            break
        hashes[grid_hash] = cycle_num
        cycle_num += 1
    cycle_size = loop_end - loop_start
    target_offset = 1000000000 % cycle_size
    current_offset = cycle_num % cycle_size
    while current_offset != target_offset:
        cycle_grid(grid)
        current_offset = (current_offset + 1) % cycle_size
    return get_load(grid)


def main() -> None:
    input_file = "Day14_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
