with open("input.txt") as file:
    X = 1 # initial value for register
    cycle = 0

    display = []
    row = ""

    cycles = set([20, 60, 100, 140, 180, 220])

    def is_matching(cycle):
        if cycle in cycles:
            return True
        return False

    strengths = 0 #signal strength
    for line in file:
        instructions = line.rstrip().split()
        if instructions[0] == "noop":
            cycle += 1


            row += "#" if len(row) in range(X - 1, X + 2) else "."
            if len(row) == 40:
                display.append(row)
                row = ""


            if is_matching(cycle):
                strengths += (X * cycle)
        if instructions[0] == "addx":
            T = 2
            while T > 0:
                cycle += 1


                row += "#" if len(row) in range(X - 1, X + 2) else "."
                if len(row) == 40:
                    display.append(row)
                    row = ""


                if is_matching(cycle):
                    strengths += (X * cycle)
                T -= 1
            X += int(instructions[1])

    print(strengths) # part1
    print(*display, sep="\n") # part 2

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

x = 1 # initialising x
x_list = [x] # store the progress here
for line in data: # go line by line
    if 'add' in line: # if we are told to add
        x_list.extend([x, x]) # add two current x
        x += int(line[5:]) # add onto x
    else: # if we get noop
        x_list.append(x)

signal_strength = sum(x_list[cycle] * cycle for cycle in range(20, len(x_list), 40))

print('The sum of the signal strengths is: ' + str(signal_strength))

for yy in range(6): # go over the rows
    crt_line = ''
    for xx in range(40): # go over the columns
        cycle = xx + yy * 40 # cycle number
        crt_line += '.' if abs(xx - x_list[cycle + 1]) <= 1 else ' ' 
    print(crt_line)















# data = []
# with open("Input10.txt") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break

#         splitted = line.strip().split(' ')
#         data.append(splitted)

# #print(data)

# mark_cycles = [20, 60, 100, 140, 180, 220]
# marked_signal_strengths = []
# cycles_elapsed = 0
# x = 1

# for line in data:
#     if line[0] == "noop":
#         cycles_elapsed += 1
#         if cycles_elapsed in mark_cycles:
#             marked_signal_strengths.append(cycles_elapsed * x)
#     else:
#         cycles_elapsed += 1
#         if cycles_elapsed in mark_cycles:
#             marked_signal_strengths.append(cycles_elapsed * x)
#         cycles_elapsed += 1
#         if cycles_elapsed in mark_cycles:
#             marked_signal_strengths.append(cycles_elapsed * x)
#         x += int(line[1])

# print(sum(marked_signal_strengths))