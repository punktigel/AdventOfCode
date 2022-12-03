
#                 Rock        Paper     Scissors
list_options = [('A','X'), ('B', 'Y'), ('C', 'Z')]

def get_number(option):
    for i in range(len(list_options)):
        if list_options[i][0] == option or list_options[i][1] == option:
            return i 


def get_points(op, my):
    indx_op = get_number(op)
    indx_me = get_number(my)

    points_round = indx_me + 1 #points from symbol
    if indx_op == indx_me: # same element - draw
        points_round += 3

    elif (indx_op + 1) % 3 == indx_me: # win
        points_round += 6
    
    return points_round


def get_max_points(file):
    sum_1 = 0
    sum_2 = 0
    with open(file, 'r') as f:
        for line in f:
            options = line.replace("\n", '').split(' ')

            sum_1 += get_points(options[0], options[1])
            sum_2 += change_option(options[0], options[1])

    print(f"Solution: \na): {sum_1}\nb): {sum_2}")

            
# Part 2:
def change_option(op_option, my_option):
    indx = get_number(op_option)
    if my_option == "X": # Lose
        return (indx -1) % 3 +1  

    elif my_option == "Y": # Draw
        return 3 + indx + 1

    else: # Win
        return 6 + (indx + 1) % 3 + 1


if __name__ == "__main__":
    get_max_points('input.txt')

"""
Part 1:
            OP  |  You      | Points    |
Rock:       A   |   X       |   1p      |   +0p     | Lose
Paper:      B   |   Y       |   2p      |   +3p     | Draw
Scissor:    C   |   Z       |   3p      |   +6p     | Win


Part 2:
X: Lose
Y: Draw
Z: Win

"""
