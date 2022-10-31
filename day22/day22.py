
inputs = [(x.strip('\n')[0:2], 
          x.strip('\n').strip('on ').strip('off ').replace('x=','').replace('y=','').replace('z=','').replace('..',',').split(',')) 
          for x in open('input1.txt')]

# def light_cubes(cube):
#     return {(x,y,z) for x in range(int(cube[1][0]),int(cube[1][1])+1)
#                     for y in range(int(cube[1][2]),int(cube[1][3])+1)
#                     for z in range(int(cube[1][4]),int(cube[1][5])+1)}

# on_cubes = {'Cant union an empty dictionary so we have this'}

# for cube in input:
#     if cube[0] == 'on':
#         on_cubes = light_cubes(cube) | on_cubes
        
#     elif cube[0] == 'of':
#         off_cubes = light_cubes(cube)
#         on_cubes = on_cubes - off_cubes

# # Part 1
# print(len(on_cubes)-1)

# Part 2

cubes = []

for input in inputs:

    switch = input[0]
    x_start, x_end = int(input[1][0]), int(input[1][1]) 
    y_start, y_end = int(input[1][2]), int(input[1][3])
    z_start, z_end = int(input[1][4]), int(input[1][5])

    cube = [switch, x_start, x_end, y_start, y_end, z_start, z_end]

    for i in cubes:
        

