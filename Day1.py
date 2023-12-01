import string


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(parsed_input: list[str]) -> int:
    total = 0
    for string in parsed_input:
        digits = [char for char in string if char.isdigit()]
        first_digit = digits[0]
        last_digit = digits[-1]
        total += int(first_digit + last_digit)
    return total


def part2(parsed_input: list[str]) -> int:
    total = 0
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digits = list(string.digits) + [digit for digit in digit_map]
    for text in parsed_input:
        first_digit, last_digit = None, None
        for i in range(len(text)):
            for digit in digits:
                if digit in text[: i + 1]:
                    if not first_digit:
                        first_digit = digit
                if digit in text[-i - 1 :]:
                    if not last_digit:
                        last_digit = digit
            if first_digit and last_digit:
                break
        if not first_digit or not last_digit:
            raise ValueError("Digits not found!")

        if first_digit in digit_map:
            first_digit = digit_map[first_digit]
        if last_digit in digit_map:
            last_digit = digit_map[last_digit]
        total += int(first_digit + last_digit)
    return total


def main() -> None:
    input_file = "Day1_input.txt"
    parsed_input = parse_input(input_file)
    part1_solution = part1(parsed_input)
    part2_solution = part2(parsed_input)
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    main()
