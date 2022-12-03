def change_array(arr, num):
    indx = 0
    for i in range(len(arr)):
        if arr[i] < arr[indx]:
            indx = i
    if num > arr[indx]:
        arr[indx] = num
 

def get_max(file):
    counter = 0
    top_three = [0 for i in range(3)] #initialize array [0,0,0]

    with open(file, 'r') as f:
        for line in f:
            if line.replace(" ", "") == "\n":
                change_array(top_three, counter)
                counter = 0

            else:
                counter += int(line)

    print(f"Solution: \na): {max(top_three)} \nb): {sum(top_three)}")


if __name__ == "__main__":
    get_max("input.txt")