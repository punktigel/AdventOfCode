def get_value(c):
    if ord(c) > 90: # a - z: 1 - 26
        return ord(c) - 97 + 1
    return ord(c) - 65 + 27 # A - Z: 27 - 52


def search_double(fst, snd):
    list = []
    for ele in fst:
        if ele in snd:
            list.append(ele)
    return list

# Part 2:
def search_three(fst, mid, lst):    
    for ele in search_double(fst, mid):
        if ele in lst:
            return get_value(ele)

def get_input(file):
    sum_1 = 0
    sum_2 = 0

    with open(file, 'r') as f:
        three_lines = []
        for line in f:
            fst = line[: int(len(line) / 2)]
            snd = line[int(len(line) / 2) :]
            sum_1 += get_value(search_double(fst, snd)[0])

            three_lines.append(line)
            if len(three_lines) >= 3:
                sum_2 += search_three(three_lines[0], three_lines[1], three_lines[2])
                three_lines = []
    
        print(f"Solution: \na): {sum_1}\nb): {sum_2}")


if __name__ == "__main__":
    get_input('input.txt')

