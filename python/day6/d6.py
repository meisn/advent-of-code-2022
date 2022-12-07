from collections import Counter


def detect_signal(inp: str, length: int):
    for i, c in enumerate(inp):
        test = inp[i : i + length]
        c = Counter(test)
        if len(c.keys()) == length:
            return test, i + length


with open("AoC22-D6.txt") as f:
    raw = f.read()

print(f"Answer 1: {detect_signal(raw, 4)}")
print(f"Answer 1: {detect_signal(raw, 14)}")
