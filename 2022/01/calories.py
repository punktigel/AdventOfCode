def set_top_three(arr, num):
    if num > min(arr):
        arr[arr.index(min(arr))] = num
 
def get_max(file):
    counter = 0
    top_three = [0 for i in range(3)]

    with open(file, 'r') as f:
        for line in f:
            if line.replace(' ', '') == "\n":
                set_top_three(top_three, counter)
                counter = 0

            else:
                counter += int(line)

    print(f"Solution: \na): {max(top_three)} \nb): {sum(top_three)}")


if __name__ == "__main__":
    get_max("input.txt")