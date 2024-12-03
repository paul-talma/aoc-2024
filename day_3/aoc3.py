import re


def get_input(path):
    with open(path, "r") as file:
        return file.read()


def process_matches(matches):
    matches = map(interpret_match, matches)
    return sum(matches)


def interpret_match(expr):
    left, right = [int(num) for num in re.findall(r"\d+", expr)]
    return left * right


def phase_1():
    matches = mul.findall(text)
    result = process_matches(matches)
    print(f"Phase 1 total: {result}")


def phase_2():
    total_pattern = re.compile(mul.pattern + "|" + do.pattern + "|" + dont.pattern)
    matches = total_pattern.findall(text)
    active = True
    sum = 0
    for match in matches:
        if match == "do()":
            active = True
        elif match == "don't()":
            active = False
        else:
            if active:
                sum += interpret_match(match)

    print(f"Phase_2 total: {sum}")


if __name__ == "__main__":
    mul = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    do = re.compile(r"do\(\)")
    dont = re.compile(r"don't\(\)")
    text = get_input("input.txt")
    phase_1()
    phase_2()
