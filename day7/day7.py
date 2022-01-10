import numpy as np 

f = open('input.txt','r')

[inputs] = [x.split(',') for x in f]

inputs = [int(x) for x in inputs]

min_value = min(inputs)
max_value = max(inputs)
array_length = len(inputs)

fuel_list1 = []
for i in range(min_value, max_value + 1):
    fuel_difference = np.array(inputs) - np.array([i]*array_length)
    required_fuel = sum(np.absolute(fuel_difference)) 
    fuel_list1.append(required_fuel)

print(min(fuel_list1))

#Part 2 

fuel_list2 = []
for i in range(min_value, max_value + 1):
    fuel_difference = np.array(inputs) - np.array([i]*array_length)
    required_fuel = np.absolute(fuel_difference)
    required_fuel_sum = sum([n*(n + 1)/2 for n in required_fuel])
    fuel_list2.append(required_fuel_sum)

print(min(fuel_list2))




