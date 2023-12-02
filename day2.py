import re


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(parsed_input: list[str]) -> int:
    total = 0
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    for game in parsed_input:
        cube_collections = re.findall(r"\d+ [a-z]+", game)
        for cubes in cube_collections:
            number, colour = cubes.split()
            if int(number) > max_cubes[colour]:
                break
        else:
            game_id = re.findall(r"^Game (\d+)", game)[0]
            total += int(game_id)
    return total


def part2(parsed_input: list[str]) -> int:
    total = 0
    for game in parsed_input:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        cube_collections = re.findall(r"\d+ [a-z]+", game)
        for cubes in cube_collections:
            number, colour = cubes.split()
            if int(number) > min_cubes[colour]:
                min_cubes[colour] = int(number)
        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        total += power
    return total


def main() -> None:
    input_file = "Day2_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
