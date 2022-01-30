import numpy as np

inputs = open('input.txt','r')
inputs = [x.strip('\n') for x in inputs]

inputs_matrix = [[10] + [int(y) for y in x] + [10] for x in inputs]
padding = [[10]*len(inputs_matrix[0])]
matrix_list = np.array(padding + inputs_matrix + padding)
energi_increase = np.array([[1]*len(matrix_list[1]) for x in range(0,12)])

flashes = 0
least_steps = []
for steps in range(0,275):
    matrix_list = matrix_list + energi_increase 
    a = np.array([x[1:11].tolist() for x in matrix_list[1:11]])
    zero_list2 = []

    while len(a[a > 9]) > 0:
        zero_list = []
        for y in range(1,11):
            for x in range(1,11):

                if matrix_list[y][x] > 9:
                
                    matrix_list[y-1][x-1] += 1
                    matrix_list[y-1][x] += 1
                    matrix_list[y-1][x+1] += 1

                    matrix_list[y+1][x-1] += 1
                    matrix_list[y+1][x] += 1
                    matrix_list[y+1][x+1] += 1

                    matrix_list[y][x-1] += 1
                    matrix_list[y][x+1] += 1

                    matrix_list[y][x] = 0
                    zero_list.append([y,x])
                    zero_list2.append([y,x])
                    flashes += 1

                    a = np.array([x[1:11].tolist() for x in matrix_list[1:11]])

        for coords in zero_list:
            matrix_list[coords[0]][coords[1]] = 0

    for coords in zero_list2:
                matrix_list[coords[0]][coords[1]] = 0
    
    b = np.array([x[1:11].tolist() for x in matrix_list[1:11]])

    if sum(sum(b)) == 0:
        least_steps.append(steps+1)

print(flashes)

# Part 2
print(least_steps[0])
        
