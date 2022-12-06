import re


instructions = []
with open(
    r"C:/Users/ronny_000/git/github/advent-of-code-2022/files/AoC22-d5_instructions.txt"
) as f:
    for line in f:
        pat = re.compile(r"(\d+)")
        move, f, t = pat.findall(line)
        it = dict(move=int(move), f=int(f), t=int(t))
        instructions.append(it)

stacks = {
    1: ["N", "R", "G", "P"],
    2: ["J", "T", "B", "L", "F", "G", "D", "C"],
    3: ["M", "S", "V"],
    4: ["L", "S", "R", "C", "Z", "P"],
    5: ["P", "S", "L", "V", "C", "W", "D", "Q"],
    6: ["C", "T", "N", "W", "D", "M", "S"],
    7: ["H", "D", "G", "W", "P"],
    8: ["Z", "L", "P", "H", "S", "C", "M", "V"],
    9: ["R", "P", "F", "L", "W", "G", "Z"],
}

# answer1
for i, instruction in enumerate(instructions):
    print(i, instruction)
    move, f, t = instruction.values()
    for _ in range(move):
        x = stacks[f].pop()
        stacks[t].append(x)

answer1 = "".join(s[-1] for s in stacks.values())
print(f"Answer1: {answer1}")

stacks = {
    1: ["N", "R", "G", "P"],
    2: ["J", "T", "B", "L", "F", "G", "D", "C"],
    3: ["M", "S", "V"],
    4: ["L", "S", "R", "C", "Z", "P"],
    5: ["P", "S", "L", "V", "C", "W", "D", "Q"],
    6: ["C", "T", "N", "W", "D", "M", "S"],
    7: ["H", "D", "G", "W", "P"],
    8: ["Z", "L", "P", "H", "S", "C", "M", "V"],
    9: ["R", "P", "F", "L", "W", "G", "Z"],
}

# answer2
for i, instruction in enumerate(instructions):
    print(i, instruction)
    move, f, t = instruction.values()
    x = stacks[f][-move:]
    print(x)
    stacks[t].extend(x)
    del stacks[f][-move:]

answer2 = "".join(s[-1] for s in stacks.values())
print(f"Answer1: {answer2}")
