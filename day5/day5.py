from collections import Counter

f = open('input.txt','r')

inputs = [x.rstrip('\n') for x in f]
inputs = [x.split(' -> ') for x in inputs]

cord1 = [x[0].split(',') for x in inputs]
cord2 = [x[1].split(',') for x in inputs]

cord1_x = [int(x[0]) for x in cord1]
cord1_y = [int(x[1]) for x in cord1]

cord2_x = [int(x[0]) for x in cord2]
cord2_y = [int(x[1]) for x in cord2]

indexlistx = []
for i,j in list(enumerate(list(zip(cord1_x,cord2_x)))):
    if j[0] == j[1]:
        indexlistx.append(i)

indexlisty = []
for i,j in list(enumerate(list(zip(cord1_y,cord2_y)))):
    if j[0] == j[1]:
        indexlisty.append(i)

l1 = []
for i in indexlistx:
    l1.append(list(map(int,cord1[i])) + list(map(int,cord2[i])))

l2 = []
for i in indexlisty:
    l2.append(list(map(int,cord1[i])) + list(map(int,cord2[i])))

points = []

for coords in l1:
    if coords[1] <= coords[3]:
        for y in range(coords[1],coords[3]+1):
            points.append([coords[0],y])
    else:
        for y in range(coords[3],coords[1]+1):
            points.append([coords[0],y])

for coords in l2:
    if coords[0] <= coords[2]:
        for x in range(coords[0],coords[2]+1):
            points.append([x,coords[1]])
    else:
        for x in range(coords[2],coords[0]+1):
            points.append([x,coords[1]])

count_points = Counter(list(map(str,points)))

count_part1 = 0 
for key, value in count_points.items():
    if value > 1:
        count_part1 = count_part1 + 1

print(count_part1)

#Part 2

a = indexlistx + indexlisty

cord = [cord1[i] + cord2[i] for i in range(len(cord1))]

indexlist45 = []
for i in sorted(a, reverse=True):
    del cord[i]

points45 = []

for coords in cord:
    c = 0 
    xpoints = [list(map(int,coords))[0], list(map(int,coords))[2]]
    ypoints = [list(map(int,coords))[1], list(map(int,coords))[3]]

    if xpoints[0] < xpoints[1] and ypoints[0] < ypoints[1]:
        for y in range(ypoints[0],ypoints[1]+1):
            points45.append([xpoints[0] + c, y]) 
            c = c + 1

    elif xpoints[0] > xpoints[1] and ypoints[0] > ypoints[1]:
        for y in range(ypoints[1],ypoints[0]+1):
            points45.append([xpoints[1] + c, y]) 
            c = c + 1

    elif xpoints[0] < xpoints[1] and ypoints[0] > ypoints[1]:
        for x in range(xpoints[0],xpoints[1]+1):
            points45.append([x, ypoints[0] + c]) 
            c = c - 1

    elif xpoints[0] > xpoints[1] and ypoints[0] < ypoints[1]:
        for x in range(xpoints[1],xpoints[0]+1):
            points45.append([x, ypoints[1] + c]) 
            c = c - 1

allpoints = points + points45

count_allpoints = Counter(list(map(str,allpoints)))

count_part2 = 0 
for key, value in count_allpoints.items():
    if value > 1:
        count_part2 = count_part2 + 1

print(count_part2)