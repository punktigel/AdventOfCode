
#                Rock(1p)   Paper(2p)  Scissors(3p)
list_options = [('A','X'), ('B', 'Y'), ('C', 'Z')]

def get_index(option):
    for i in range(len(list_options)):
        if list_options[i][0] == option or list_options[i][1] == option:
            return i 


def get_points(indx_op, indx_me):
    if (indx_op + 1) % 3 == indx_me: # Win
        return 6 + indx_me + 1

    elif indx_op == indx_me: # Draw
        return 3 + indx_me + 1

    return indx_me + 1 # Lose
      
# Part 2:
def change_option(indx, my_option):
    if my_option == "Z": # Win
        return 6 + (indx + 1) % 3 + 1

    elif my_option == "Y": # Draw
        return 3 + indx + 1

    return (indx -1) % 3 + 1 # Lose


def get_max_points(file):
    sum_1 = 0
    sum_2 = 0
    with open(file, 'r') as f:
        for line in f:
            options = line.replace("\n", '').split(' ')

            sum_1 += get_points(get_index(options[0]), get_index(options[1]))
            sum_2 += change_option(get_index(options[0]), options[1])

    print(f"Solution: \na): {sum_1}\nb): {sum_2}")

if __name__ == "__main__":
    get_max_points('input.txt')

"""
Part 1:
            Fst |  Snd  | Points    |
Rock:       A   |   X   |   1p      |   +0p     | Lose
Paper:      B   |   Y   |   2p      |   +3p     | Draw
Scissor:    C   |   Z   |   3p      |   +6p     | Win


Part 2:
X: Lose
Y: Draw
Z: Win

"""
