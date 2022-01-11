import numpy as np 
import itertools

f = open('input.txt','r')
inputs = [x.strip('\n') for x in f]

matrixlist = []
for numbers in inputs:
    matrixlist.append([9] + [int(x) for x in numbers] + [9])

pad = [len(matrixlist[0])*[9]]
matrix = np.array(pad + matrixlist + pad)

low_points = []
basinplacement = [] # for part 2
for row in range(1,len(matrix)-1):

    for column in range(1,len(matrix[0])-1):
        element = matrix[row][column]
        up = matrix[row-1][column]
        down = matrix[row+1][column]
        left = matrix[row][column-1]
        right = matrix[row][column+1]

        if element < up and element < down and element < left and element < right:
            low_points.append(element)
            basinplacement.append([row,column])

sum([x+1 for x in low_points])

#Part 2

matrix_new = matrix.tolist()
matrix_new = np.array(matrix_new)

for x in matrix_new:
    for n, y in enumerate(x):
        if y != 9:
            x[n] = 1

def basin_size(coords,matrix):

    # a for loop that expands depending on the size of the basin 
    for coord in coords:
        row = coord[0]
        column = coord[1]
        matrix[row][column] = 0

        up = matrix[row-1][column]
        down = matrix[row+1][column]
        left = matrix[row][column-1]
        right = matrix[row][column+1]

        if up != 9 and up != 0:
            coords.append([row-1,column])
        if down != 9 and down != 0:
            coords.append([row+1,column])
        if left != 9 and left != 0:
            coords.append([row,column-1])
        if right != 9 and right != 0:
            coords.append([row,column+1])

    # there will be duplicates, simply remove it 
    coords.sort() 
    return len(list(coords for coords,_ in itertools.groupby(coords)))

all_basin_sizes = []
for basin in basinplacement:
    all_basin_sizes.append(basin_size([basin],matrix_new))

sorted_sizes = sorted(all_basin_sizes,reverse=True)

print(sorted_sizes[0]*sorted_sizes[1]*sorted_sizes[2])