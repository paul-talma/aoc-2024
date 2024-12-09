def get_input(path):
    with open(path, "r") as file:
        equations = file.readlines()
        equations = [line.strip().split(":") for line in equations]
        equations = [(int(eq[0]), [int(x) for x in eq[1].split()]) for eq in equations]
        return equations


def is_valid(target, curr_val, remaining_vals):
    if not remaining_vals:
        return target == curr_val
    next_val = remaining_vals[0]
    times_val = curr_val * next_val
    plus_val = curr_val + next_val
    remaining_vals = remaining_vals[1:]
    if times_val > target and plus_val > target:
        return False
    if times_val > target:
        return is_valid(target, plus_val, remaining_vals)
    return is_valid(target, plus_val, remaining_vals) or is_valid(
        target, times_val, remaining_vals
    )


def phase_1():
    return sum([eq[0] for eq in equations if is_valid(eq[0], eq[1][0], eq[1][1:])])


def concat(x, y):
    return int(str(x) + str(y))


def is_valid_2(target, curr_val, remaining_vals):
    if not remaining_vals:
        return target == curr_val

    next_val = remaining_vals[0]
    times_val = curr_val * next_val
    plus_val = curr_val + next_val
    concat_val = concat(curr_val, next_val)

    if all([x > target for x in [times_val, plus_val, concat_val]]):
        return False

    remaining_vals = remaining_vals[1:]

    if times_val > target and concat_val > target:
        return is_valid_2(target, plus_val, remaining_vals)
    if plus_val > target and concat_val > target:
        return is_valid_2(target, times_val, remaining_vals)
    if plus_val > target and times_val > target:
        return is_valid_2(target, concat_val, remaining_vals)

    if times_val > target:
        return is_valid_2(target, concat_val, remaining_vals) or is_valid(
            target, plus_val, remaining_vals
        )
    if plus_val > target:
        return is_valid_2(target, concat_val, remaining_vals) or is_valid(
            target, times_val, remaining_vals
        )
    if concat_val > target:
        return is_valid_2(target, plus_val, remaining_vals) or is_valid(
            target, times_val, remaining_vals
        )

    return (
        is_valid_2(target, plus_val, remaining_vals)
        or is_valid_2(target, times_val, remaining_vals)
        or is_valid_2(target, concat_val, remaining_vals)
    )


def phase_2():
    return sum([eq[0] for eq in equations if is_valid_2(eq[0], eq[1][0], eq[1][1:])])


if __name__ == "__main__":
    equations = get_input("input.txt")
    print(phase_1())
    print(phase_2())

