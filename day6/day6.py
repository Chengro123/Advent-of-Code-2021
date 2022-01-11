import numpy as np 
from collections import Counter


start = time.time()

f = open('input.txt','r')

[inputs] = [x.split(',') for x in f]
inputs = list(map(int,inputs))

count = 0
for i in range(1,120):
    count = count + 1
    new_fish = 0 
    for j,fish in enumerate(inputs):
        if fish == 0:
            inputs[j] = 6
            new_fish = new_fish + 1
        else:
            inputs[j] = inputs[j] - 1
    inputs = inputs + [8]*new_fish
    print(count)

end = time.time()
print(end - start)

print(len(inputs))



#Part 2 
# jälva noob bait asså

fish_chain = [[0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0]]
sorted(Counter(inputs).items()) 

# extracted manually 
fishes = [0,191,30,20,35,24,0,0,0]

print(np.matmul(np.matrix(fish_chain) ** 256, np.array(fishes).transpose(),dtype=np.int64).sum())