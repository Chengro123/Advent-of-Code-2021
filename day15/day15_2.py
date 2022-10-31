import numpy as np
import heapq

map = np.genfromtxt("input.txt", dtype=int, delimiter=1)
height, width = map.shape

def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in neighbors if 0 <= a < width and 0 <= b < height]

def search(map):
    queue = [(0, (0, 0))]
    while True:
        risk, (x, y) = heapq.heappop(queue)
        
        if (x, y) == (width - 1, height - 1):
            return risk

        for a, b in get_neighbors(x, y):
            if map[b][a] >= 0:
                heapq.heappush(queue, (risk+(map[b][a]), (a,b)))
                map[b][a] = -1

print(search(map))

# Part 2

map = np.genfromtxt("input.txt", dtype=int, delimiter=1)
map = np.concatenate([map+i for i in range(5)], axis=0)
map = np.concatenate([map+i for i in range(5)], axis=1)

height, width = map.shape

for i in range(height):
    for j in range(width):
        if map[i][j] > 9:
            map[i][j] = map[i][j] % 9

print(search(map))

