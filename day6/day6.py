# import numpy as np 
from collections import Counter

# f = open('input.txt','r')

# [inputs] = [x.split(',') for x in f]
# inputs = list(map(int,inputs))

# count = 0
# for i in range(1,250):
#     count = count + 1
#     new_fish = 0 
#     for j,fish in enumerate(inputs):
#         if fish == 0:
#             inputs[j] = 6
#             new_fish = new_fish + 1
#         else:
#             inputs[j] = inputs[j] - 1
#     inputs = inputs + [8]*new_fish
#     print(count)

# print(len(inputs))



#Part 2 

# jälva noob bait asså

import numpy as np 
f = open('input.txt','r')

[inputs] = [x.split(',') for x in f]
inputs = list(map(int,inputs))

count = 0 
for i in range(1,257):
    count = count + 1
    new_fish = 0 
    new_fish = Counter(inputs)[0]
    inputs = [x if x != 0 else 7 for x in inputs]
    inputs = np.array(inputs) - np.array([1]*len(inputs))
    inputs = list(inputs) + [8]*new_fish
    print(count)