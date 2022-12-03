with open("./files/AoC22-d1.txt") as f:
    raw = f.read()

inp = []
for i, it in enumerate(raw.split("\n\n")):

    dat = [int(i) for i in it.split("\n")]
    s = sum(dat)
    inp.append((i, it, s))

inp.sort(key=lambda x: x[2], reverse=True)
answer1 = inp[0][2]
answer2 = sum(i[2] for i in inp[:3])
print(f"Answer 1: {answer1}")
print(f"Answer 2: {answer2}")
