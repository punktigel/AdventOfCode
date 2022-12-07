
def delete_smallest(arr):
    del_arr = []
    needed = 30000000
    space = 70000000 - arr[0]
    
    for ele in arr:
        if ele + space >= needed:
            del_arr.append(ele)
    return min(del_arr)

def sum_dir(arr):
    arr_sum = []
    for dir in arr:
        sum = 0
        for ele in dir:
            if ele != dir[0]:
                sum += int(ele[0])
        arr_sum.append([dir[0], sum])

    for i in range(len(arr_sum)):
        for j in range(len(arr_sum)):
            if arr_sum[i][0] in arr_sum[j][0] and i != j:
                arr_sum[i][1] += arr_sum[j][1]

    sol_1 = 0
    for i in range(len(arr_sum)):
        if arr_sum[i][1] <= 100000:
            sol_1 += arr_sum[i][1]

    arr_values = []
    for ele in arr_sum:
        arr_values.append(ele[1])

    

    sol_2 = delete_smallest(arr_values)
    print(f"Solution: \na): {sol_1}\nb): {sol_2}")

def get_path(arr, dir=""):
    ret = ""
    for ele in arr:
        ret += ele
    
    return ret + dir

def find_dir(arr, path):
    for i in range(len(arr)):
        if arr[i][0] == path:
            return i

def change_dir(path, value):
    if value == '/':
        path = ['/']
    elif value == '..':
        path.pop(len(path) - 1)
    else:
        path.append(value)

def add_files(values, arr, path):
    if values[0] == 'dir':
        arr.append([get_path(path, values[1])])
    else:
        indx = find_dir(arr, get_path(path))
        arr[indx].append(values)

def get_directory(lines):
    arr_files = [['/']]
    dir_path = ['/']

    for line in lines:
        values = line.split(' ')
        if line == '' or values[1] == 'ls':
            continue

        if values[1] == 'cd': # change directory
            change_dir(dir_path, values[2])

        else:
            add_files(values, arr_files, dir_path)

    sum_dir(arr_files)


def get_input(file):
    with open(file, 'r') as f:
        txt = f.read()

    lines = txt.split('\n')
    get_directory(lines)

if __name__ == "__main__":
    get_input('input.txt')
