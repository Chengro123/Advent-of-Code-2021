from collections import Counter

inputs = open('input.txt','r')
inputs = [x.strip('\n') for x in inputs]
pairs = [x.split('-') for x in inputs]

all_caves = list(set([x for pair in pairs for x in pair]))

all_neighbour = {}
for caves in all_caves:
    neighbour = []
    neighbour.append(caves)
    for pair in pairs:
        if caves in pair:
            neighbour.append(pair[0])
            neighbour.append(pair[1])
    neighbour = list(set(neighbour))
    neighbour.remove(caves)
    all_neighbour.update({caves:neighbour})


def explore_caves(caves, starting_cave, already_visited):
    total_ways = 0 

    if starting_cave =='end':
        return 1 

    else: 
        neighbours = caves[starting_cave]

        if starting_cave.islower():
            already_visited.append(starting_cave)
        visited_copy = already_visited.copy()    

        for neighbour in neighbours:
            if neighbour not in already_visited:
                total_ways = total_ways + explore_caves(caves,neighbour,already_visited)
                already_visited = visited_copy.copy()

    return total_ways

print(explore_caves(all_neighbour.copy(), 'start', []))

# Part 2 

# Same but different 
def explore_caves_2(caves, starting_cave, already_visited):
    total_ways = 0 

    if starting_cave =='end':
        return 1 

    else: 
        neighbours = caves[starting_cave]

        if starting_cave.islower():
            already_visited.append(starting_cave)
        visited_copy = already_visited.copy()    

        for neighbour in neighbours:
            if list(Counter(already_visited).values()).count(2) < 2 and already_visited.count(neighbour) < 2 and neighbour != 'start':
                total_ways = total_ways + explore_caves_2(caves,neighbour,already_visited)
                already_visited = visited_copy.copy()

    return total_ways

print(explore_caves_2(all_neighbour.copy(), 'start', []))