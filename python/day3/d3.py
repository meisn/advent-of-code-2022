import string

from dataclasses import dataclass

import more_itertools


@dataclass
class Record:
    """Holding the data, mainly to have convinient
    way to access fields (as opposed to dict).

    The only field of relevance being 'common'
    rest is purely for debug/tests."""

    line: str
    length: int
    s1: set[str]
    s2: set[str]
    common: str


@dataclass
class Record2:
    """Holding the data, mainly to have convinient
    way to access fields (as opposed to dict).

    The only field of relevance being 'common'
    rest is purely for debug/tests."""

    chunk: list[str]
    s1: str
    s2: str
    s3: str
    common: str


def read_input():
    raw = []
    with open("./files/AiC22-d3.txt") as f:

        for line in f:
            raw.append(line.strip())
        return raw


def get_answer1(rawinput: list[str]):
    """Generating dataclass by dividing lines."""

    for line in rawinput:
        line = line.strip()
        l = len(line)
        s = l // 2
        s1 = set(line[:s])
        s2 = set(line[s:])
        common = list(s1 & s2)[0]
        it = Record(line=line, length=l, s1=s1, s2=s2, common=common)

        yield it


def get_answer2(rawinput: list[str]):
    """Generating dataclass by chunking lines."""
    for chunk in more_itertools.chunked(rawinput, 3):
        s1, s2, s3 = chunk
        common = list(set(s1) & set(s2) & set(s3))[0]
        it = Record2(chunk=chunk, s1=s1, s2=s2, s3=s3, common=common)
        yield it


def assign_priority(letter: str):
    return PRIORITY.get(letter, 0)


PRIORITY = {
    c: i
    for i, c in enumerate(
        string.ascii_lowercase + string.ascii_uppercase, start=1
    )
}

if __name__ == "__main__":
    raw = read_input()

    answer1 = sum(
        assign_priority(record.common) for record in get_answer1(raw)
    )
    print(f"Answer1: {answer1}")

    answer2 = sum(
        assign_priority(record.common) for record in get_answer2(raw)
    )
    print(f"Answer1: {answer2}")
