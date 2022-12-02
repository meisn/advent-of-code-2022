opponent = dict(zip("ABC", range(1, 4)))
player = dict(zip("XYZ", range(1, 4)))
results = dict(zip("XYZ", range(3)))

def calc_result1(opponent_in: str, player_in: str) -> int:
    o_val = opponent.get(opponent_in, 0)
    p_val = player.get(player_in, 0)
    res = p_val - o_val
    ret = 0
    match res:
        case 0:
            ret = 3
        case 1:
            ret = 6
        case 2:
            ret = 0
        case -1:
            ret = 0
        case -2:
            ret = 6
    return ret + p_val


def calc_result2(opponent_in: str, player_in: str) -> int:
    
    val = ""
    match (opponent_in, player_in):
        case ('A', 'X'):
            val = 'C'
        case ('A', 'Y'):
            val = 'A'
        case ('A', 'Z'):
            val = 'B'
        case ('B', 'X'):
            val = 'A'
        case ('B', 'Y'):
            val = 'B'
        case ('B', 'Z'):
            val = 'C'
        case ('C', 'X'):
            val = 'B'
        case ('C', 'Y'):
            val = 'C'
        case ('C', 'Z'):
            val = 'A'
    
    result = results.get(player_in, 0)
    p_val = opponent.get(val, 0)
    return result * 3 + p_val

if __name__ == "__main__":

    with open("./files/AoC22-d2.txt") as f:
        raw = []
        for line in f:
            i, o = line.strip().split()
            raw.append((i, o))

    answer1 = sum(calc_result1(*r) for r in raw)
    print(f"Answer1:  {answer1}")
    answer2 = sum(calc_result2(*r) for r in raw)
    print(f"Answer2:  {answer2}")
