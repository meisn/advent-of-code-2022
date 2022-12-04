raw = []
with open("./files/AoC22-d4.txt") as f:
    for line in f:
        raw.append(line.strip().split(","))


def check_sections(range_input: list[str]):
    """Check if the ranges are supersets"""
    p1, p2 = range_input
    start1, end1 = p1.split("-")
    s1 = set(range(int(start1), int(end1) + 1))
    start2, end2 = p2.split("-")
    s2 = set(range(int(start2), int(end2) + 1))
    return s1.issuperset(s2) or s2.issuperset(s1)


def check_overlap(range_input: list[str]):
    """Check if ranges intersect."""
    p1, p2 = range_input
    start1, end1 = p1.split("-")
    s1 = set(range(int(start1), int(end1) + 1))
    start2, end2 = p2.split("-")
    s2 = set(range(int(start2), int(end2) + 1))
    return bool(s1.intersection(s2))


answer1 = sum(check_sections(r) for r in raw)
print(f"Answer1: {answer1}")
answer2 = sum(check_overlap(r) for r in raw)
print(f"Answer1: {answer2}")
