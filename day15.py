import re


def parse_input(input_file: str) -> str:
    with open(input_file) as f:
        return f.read().strip()


def hash_algorithm(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part1(parsed_input: str) -> int:
    total = 0
    for string in parsed_input.split(","):
        total += hash_algorithm(string)
    return total


def get_focusing_power(boxes: list[dict[str, int]]):
    total = 0
    for box_idx, box in enumerate(boxes, start=1):
        for label_idx, label in enumerate(box, start=1):
            total += box_idx * label_idx * int(box[label])
    return total


def part2(parsed_input: str) -> int:
    boxes: list[dict[str, int]] = [{} for _ in range(256)]
    for string in parsed_input.split(","):
        label, operation = re.findall(r"([a-z]+)([-=]\d*)", string)[0]
        box_num = hash_algorithm(label)
        current_box = boxes[box_num]
        if operation[0] == "=":
            current_box[label] = operation[1:]
        elif operation[0] == "-":
            if label in current_box:
                current_box.pop(label)
    return get_focusing_power(boxes)


def main() -> None:
    input_file = "Day15_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
