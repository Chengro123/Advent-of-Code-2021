inputs = open('input.txt','r')
inputs2 = open('string.txt','r')

combinations = [(x.strip('\n')).split(' -> ') for x in inputs]
string = [x for x in inputs2][0]

zero_dict = {}
comb_dict = {}
for pair in combinations:
    zero_dict[pair[0]] = 0
    comb_dict[pair[0]] = pair[1]

pair_dict = zero_dict.copy()

for i in range(0,len(string)-1):
    if string[i:i+2] in pair_dict:
        pair_dict[string[i:i+2]] += 1

def expand_list(pair_dict, zero_dict, comb_dict):
    for pair, n in pair_dict.items():
        if n != 0:
            zero_dict[pair[0] + comb_dict[pair]] += n
            zero_dict[comb_dict[pair] + pair[1]] += n
    return zero_dict

for s in range(0,40):
    pair_dict = expand_list(pair_dict.copy(), zero_dict.copy(), comb_dict)

def count_occurence(dictionary):
    counts = {}
    for pair, n in dictionary.items():
        if pair[0] in counts:
            counts[pair[0]] += n
        else:
            counts[pair[0]] = n

        if pair[1] in counts:
            counts[pair[1]] += n
        else:
            counts[pair[1]] = n
    for pair, n in counts.items():
        counts[pair] = n/2

    return counts

print(count_occurence(pair_dict))
stats = count_occurence(pair_dict)
print(max(stats, key=stats.get))
print(min(stats, key=stats.get))

# Do it manually, could probably do everything in few rows