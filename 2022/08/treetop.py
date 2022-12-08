def add_list(arr, i, j, ele):
    if arr == [] or (i,j,ele) not in arr:
        arr.append((i,j, ele))

def calc_view(arr, updown,lr):
    ret = []
    height = arr[updown][lr]

    if updown == 0 or updown == len(arr) -1 or lr == 0 or lr == len(arr[0]) - 1:
        return 0

    # look left
    idx = lr - 1
    while idx > 0:
        if arr[updown][idx] >= height:
            break
        idx -= 1
    ret.append(lr - idx)

    #look right
    idx = lr + 1
    while idx < len(arr[0]) -1:
        if arr[updown][idx] >= height:
            break
        idx += 1
    ret.append(idx - lr)

    # look up
    idx = updown - 1
    while idx > 0:
        if arr[idx][lr] >= height:
            break
        idx -= 1
    ret.append(updown - idx)

    # look down
    idx = updown + 1
    while idx < len(arr) -1:
        if arr[idx][lr] >= height:
            break
        idx += 1
    ret.append(idx - updown)

    sol = 1
    for ele in ret:
        sol *= ele
    return sol

def get_scenic_score(arr):
    max_view = 0
    for i in range(len(arr)): # up down
        for j in range(len(arr)): # left right
            view = calc_view(arr, i, j)
            if view > max_view:
                max_view = view
    return max_view


def get_trees(arr, pos):
    top = [-1 for i in range(len(arr[0]))]
    bottom = [-1 for i in range(len(arr[0]))]

    for v in range(len(arr)): # vertical

        front = -1
        end = -1

        for h in range(len(arr[v])): # horizontal
            # forward
            if front < arr[v][h]:
                add_list(pos, v,h, arr[v][h])
                front = arr[v][h]

            # down
            if top[h] < arr[v][h]:
                add_list(pos, v, h, arr[v][h])
                top[h] = arr[v][h]
            
            # up
            i_up = len(arr) -1 -v
            if bottom[h] < arr[i_up][h]:
                add_list(pos, i_up, h, arr[i_up][h])
                bottom[h] = arr[i_up][h]

            # backwards
            h = len(arr[v]) -1 -h
            if end < arr[v][h]:
                add_list(pos, v,h, arr[v][h])
                end = arr[v][h]

    return len(pos)


def get_input(file):
    with open(file, 'r') as f:
        txt = f.read().split('\n')

    lines = []
    for line in txt:
        lines.append([int(value) for value in line])
    
 
    sol_1 = get_trees(lines, [])
    sol_2 = get_scenic_score(lines)
    print(f"Solution: \na): {sol_1}\nb): {sol_2}")


if __name__ == "__main__":
    get_input('input.txt')