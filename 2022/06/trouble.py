
def all_diff(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                return False
    return True
    
def get_characters(txt, num):
    arr_num = []

    for i in range(len(txt)):
        if len(arr_num) < num:
            arr_num.append(txt[i])
            
        else:
            arr_num.pop(0)
            arr_num.append(txt[i])

        
        if all_diff(arr_num) and len(arr_num) == num:
            return i + 1

def get_input(file):
    with open(file, 'r') as f:
        txt = f.read()

    sol_1 = get_characters(txt, 4)
    sol_2 = get_characters(txt, 14)

    print(f"Solution: \na): {sol_1}\nb): {sol_2}")

if __name__ == "__main__":
    get_input('input.txt')