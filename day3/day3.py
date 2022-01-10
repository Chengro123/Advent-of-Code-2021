f = open('input.txt','r')
l = [x.rstrip("\n") for x in f]

nth_column = [[int(x[n]) for x in l] for n in range(0,12)]
column_sum = [sum(x) for x in nth_column]
gamma_rate = [1 if x > len(l)/2 else 0 for x in column_sum]
epsilon_rate = [0 if x > len(l)/2 else 1 for x in column_sum]

gamma = ''.join(map(str, gamma_rate))
epsilon = ''.join(map(str, epsilon_rate))

print(int(gamma,2)*int(epsilon,2))

#Part 2

f = open('input.txt','r')
l = [x.rstrip("\n") for x in f]

index = 0
while len(l) > 1:
    count1 = 0
    count0 = 0
    list1 = []
    list0 = []
    for x in l:
        if int(x[index]) == 1:
            count1 = count1 + 1
            list1.append(x)
        elif int(x[index]) == 0:
            count0 = count0 + 1 
            list0.append(x)

    if count1 >= count0:
        l = list1
    else:
        l = list0 
    index = index + 1
a = ''.join(l)
oxygen = int(a,2)

f = open('input.txt','r')
l = [x.rstrip("\n") for x in f]

index = 0
while len(l) > 1:
    count1 = 0
    count0 = 0
    list1 = []
    list0 = []
    for x in l:
        if int(x[index]) == 1:
            count1 = count1 + 1
            list1.append(x)
        elif int(x[index]) == 0:
            count0 = count0 + 1 
            list0.append(x)

    if count1 >= count0:
        l = list0
    else:
        l = list1
    index = index + 1
b = ''.join(l)
co2 = int(b,2)

print(oxygen*co2)



    


