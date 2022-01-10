f = open('input.txt','r')

inputs = [x.rstrip('\n') for x in f]
inputs = [(x.replace('|','')).split() for x in inputs]

outputvalue = [x[10:14] for x in inputs]

# we count string with length 2, 3, 4, 7 

count = 0 
for i in outputvalue:
    for j in i:
        if len(j) in [2,3,4,7]:
            count = count + 1

print(count)


#Part 2

value = [x[0:10] for x in inputs]

sortedoutputvalue = [list(map(sorted,x)) for x in outputvalue]
sortedoutputvalue = [list(map(''.join,x)) for x in sortedoutputvalue]

for k, x in enumerate(sortedoutputvalue):
    one = [i for i in value[k] if len(i) == 2][0] 
    one = [i for i in one]

    four = [i for i in value[k] if len(i) == 4][0] 
    four = [i for i in four]

    seven = [i for i in value[k] if len(i) == 3][0]
    seven = [i for i in seven]

    for n, y in enumerate(x):

        if len(y) in [2,3,4,7]: #correspond to 1 7 4 8
            if len(y) == 2:
                x[n] = 1
            elif len(y) == 3:
                x[n] = 7
            elif len(y) == 4:
                x[n] = 4
            elif len(y) == 7:
                x[n] = 8

        elif len(y) == 5:
            union = four + [s for s in [t for t in y] if s not in four]
            snitt = list(set(four) & set(y))

            if (one[0] in y) and (one[1] in y):
                x[n] = 3 

            elif len(list(set(union)-set(snitt))) == 5:
                x[n] = 2 
            else:
                x[n] = 5 

        elif len(y) == 6:
            union = four + [s for s in [t for t in y] if s not in four]
            snitt = list(set(four) & set(y))

            if len(list(set(union)-set(snitt))) == 2:
                x[n] = 9

            elif (seven[0] in y) and (seven[1] in y) and (seven[2] in y):

                x[n] = 0 
            
            else: 
                x[n] = 6
    

print(sum([int(''.join(map(str,x))) for x in sortedoutputvalue]))