def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def get_starting_location(grid: list[list[str]]) -> tuple[int, int]:
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            char = grid[row_idx][col_idx]
            if char == "S":
                return (row_idx, col_idx)
    raise ValueError("Starting Location not found")


def get_new_direction(
    grid: list[list[str]], current_location: tuple[int, int], direction: str
) -> str | None:
    char_mapping = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    try:
        char = grid[current_location[0] + char_mapping[direction][0]][
            current_location[1] + char_mapping[direction][1]
        ]
    except IndexError:
        return None
    direction_mapping = {
        "N": {"|": "N", "7": "W", "F": "E"},
        "E": {"-": "E", "7": "S", "J": "N"},
        "S": {"|": "S", "L": "E", "J": "W"},
        "W": {"-": "W", "L": "N", "F": "S"},
    }
    return direction_mapping[direction].get(char, None)


def get_starting_direction(
    grid: list[list[str]], current_location: tuple[int, int]
) -> str:
    if grid[current_location[0] - 1][current_location[1]] in (
        "|",
        "7",
        "F",
    ) and get_new_direction(grid, current_location, "N"):
        return "N"
    if grid[current_location[0]][current_location[1] + 1] in (
        "-",
        "7",
        "J",
    ) and get_new_direction(grid, current_location, "E"):
        return "E"
    if grid[current_location[0] + 1][current_location[1]] in (
        "|",
        "L",
        "J",
    ) and get_new_direction(grid, current_location, "S"):
        return "S"
    if grid[current_location[0]][current_location[1] - 1] in (
        "-",
        "L",
        "F",
    ) and get_new_direction(grid, current_location, "W"):
        return "W"
    raise ValueError("Unable to get starting direction")


def inside_maze_check(
    row_idx: int,
    col_idx: int,
    grid: list[list[str]],
    visited_nodes: set[tuple[int, int]],
):
    count = 0
    north_chars = {"|", "L", "J"}
    for temp_col_idx in range(col_idx, len(grid[0])):
        if (
            grid[row_idx][temp_col_idx] in north_chars
            and (row_idx, temp_col_idx) in visited_nodes
        ):
            count += 1
    return count % 2 != 0


def replace_starting_location(
    starting_direction: str,
    final_direction: str,
    grid: list[list[str]],
    starting_location: tuple[int, int],
) -> None:
    mapping = {
        "EE": "-",
        "WW": "-",
        "NN": "|",
        "SS": "|",
        "NW": "L",
        "ES": "L",
        "NE": "J",
        "WS": "J",
        "WN": "7",
        "SE": "7",
        "SW": "F",
        "EN": "F",
    }
    grid[starting_location[0]][starting_location[1]] = mapping[
        starting_direction + final_direction
    ]


def solve(parsed_input: list[str], part: int = 1) -> int:
    grid: list[list[str]] = [list(line) for line in parsed_input]
    starting_location: tuple[int, int] = get_starting_location(grid)
    current_location = starting_location
    starting_direction = get_starting_direction(grid, current_location)
    current_direction = starting_direction
    visited_nodes = {starting_location}
    distance = 0
    while True:
        if current_direction == "N":
            new_direction = get_new_direction(grid, current_location, "N")
            new_location = (current_location[0] - 1, current_location[1])
        elif current_direction == "E":
            new_direction = get_new_direction(grid, current_location, "E")
            new_location = (current_location[0], current_location[1] + 1)
        elif current_direction == "S":
            new_direction = get_new_direction(grid, current_location, "S")
            new_location = (current_location[0] + 1, current_location[1])
        elif current_direction == "W":
            new_direction = get_new_direction(grid, current_location, "W")
            new_location = (current_location[0], current_location[1] - 1)
        else:
            raise ValueError("Current_direction not in NESW")
        distance += 1
        if grid[new_location[0]][new_location[1]] == "S":
            replace_starting_location(
                starting_direction, current_direction, grid, starting_location
            )
            break
        if not new_direction:
            raise ValueError("Broken Cycle")
        current_location = new_location
        current_direction = new_direction
        visited_nodes.add(current_location)
    if part == 1:
        return distance // 2
    total_inside_circle = 0
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if (row_idx, col_idx) not in visited_nodes:
                inside_circle = inside_maze_check(row_idx, col_idx, grid, visited_nodes)
                if inside_circle:
                    total_inside_circle += 1
    return total_inside_circle


def main() -> None:
    input_file = "Day10_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = solve(parsed_input, part=1)
    part2_solution = solve(parsed_input, part=2)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
