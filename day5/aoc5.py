def get_input(path):
    with open(path, "r") as file:
        return file.readlines()


def get_rules(text):
    rules = []
    for line in text:
        if line != "\n":
            left, right = line.strip().split("|")
            rules.append((int(left), int(right)))
        else:
            break
    return rules


def get_updates(text):
    updates = []
    for line in text[text.index("\n") + 1 :]:
        updates.append([int(num) for num in line.split(",")])
    return updates


def is_valid(update):
    for id, num in enumerate(update):
        for rule in rules:
            left, right = rule
            if left == num:
                if right in update[:id]:
                    return False
    return True


def get_middle(update):
    return update[len(update) // 2]


def sum_valid_updates():
    return sum([get_middle(update) for update in updates if is_valid(update)])


def get_invalid_updates(updates):
    return [update for update in updates if not is_valid(update)]


def conflict_idx(update):
    for id, num in enumerate(update):
        for rule in rules:
            left, right = rule
            if left == num:
                if right in update[:id]:
                    conflict_id = update.index(right)
                    return id, conflict_id


def fix_update(update):
    while not is_valid(update):
        right, left = conflict_idx(update)
        temp = update.pop(left)
        update = update[:right] + [temp] + update[right:]
    return update


def sum_invalid_updates():
    corrected_updates = map(fix_update, get_invalid_updates(updates))
    return sum([get_middle(update) for update in corrected_updates])


if __name__ == "__main__":
    text = get_input("input.txt")
    rules = get_rules(text)
    updates = get_updates(text)
    print(f"Phase 1: {sum_valid_updates()}")
    print(f"Phase 2: {sum_invalid_updates()}")
