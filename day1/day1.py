f = open('input.txt','r')
l = [int(x.rstrip("\n")) for x in f]

list1 = l[:-1]
list2 = l[1:]
difference = []

zip_object = zip(list1, list2)
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)
print(sum([x<0 for x in difference]))

#Part 2

l_sum = [l[x] + l[x+1] + l[x+2] for x in range(0,len(l)-2)]

list1 = l_sum[:-1]
list2 = l_sum[1:]
difference = []

zip_object = zip(list1, list2)
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)
print(sum([x<0 for x in difference]))


