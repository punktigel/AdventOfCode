replace = ['move', ' from', ' to', '\n']

def filter_instr(instr):
    for rep in replace:
        instr = instr.replace(rep, '')
    instr = instr.strip()

    num, start, end = instr.split(' ')

    return int(num), int(start) - 1, int(end) - 1


def stack_mover(instr, arr):
    num, start, end = filter_instr(instr)

    for i in range(num):
        arr[end].insert(0, arr[start][0])
        arr[start].pop(0)
# Part 2
def mover9001(instr, arr):
    num, start, end = filter_instr(instr)

    for i in range(num):
        arr[end].insert(i, arr[start][0])
        arr[start].pop(0)

    
def get_stacks(line, arr):
    while len(line) // 4 > len(arr):
        arr.append([])
    for i in range(len(line)):
        if i % 4 == 1 and line[i] != ' ':
            arr[i // 4].append(line[i])

def get_input(file):
    with open(file, 'r') as f:
        arr_stack_1 = []
        arr_stack_2 = []
        instr = False

        for line in f:
            if instr:
                stack_mover(line, arr_stack_1)
                mover9001(line, arr_stack_2)

            elif line.find('1') == -1:
                get_stacks(line, arr_stack_1)
                get_stacks(line, arr_stack_2)
            if line == "\n":
                instr = True
        
        ans_1 = ""
        ans_2 = ""
        for i in range(len(arr_stack_1)):
            ans_1 += arr_stack_1[i][0]
            ans_2 += arr_stack_2[i][0]
        
        print(f"Solution: \na): {ans_1}\nb): {ans_2}")


if __name__ == "__main__":
    get_input('input.txt')

