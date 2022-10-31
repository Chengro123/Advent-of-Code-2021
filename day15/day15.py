inputs = open('input2.txt','r')
inputs = [x.split('\n') for x in inputs]

for x in inputs[0:len(inputs)-1]:
    del x[1]

inputs = [x for y in inputs for x in y]

risk_dict = {}

for y, risk_row in enumerate(inputs):
    for x, risk in enumerate(risk_row):
        risk_dict[(x,y)] = int(risk)


def remove_coords(visited, visited_at):
    removing = []

    for x,y,z in visited_at:

        if x == 0 and y == 0:
            if (x+1,y) and (x,y+1) in visited:
                removing.append((x,y,z))

        elif x == 0:
            if (x+1,y) and (x,y+1) and (x,y-1) in visited:
                removing.append((x,y,z))
            
        elif y == 0:
            if (x+1,y) and (x,y+1) and (x-1,y) in visited:
                removing.append((x,y,z))
        
        else: 
            if (x+1,y) and (x,y+1) and (x-1,y) and (x,y-1) in visited:
                removing.append((x,y,z))

    for r in removing:
        visited_at.remove(r)

    return visited_at
    

visited = [(0,0,0)] 
visited_at = [(0,0,0)]
visited_coord = []
destination = len(inputs) - 1
s = 10

while (destination,destination) not in visited_coord:
    largest = []

    for x,y,cost in visited_at:

        if (x+1,y) not in visited_coord:
            try:
                risk_dict[(x+1,y)]
            except:
                None
            else:
                largest.append((x+1, y, cost + risk_dict[(x+1,y)]))
        
        if (x-1,y) not in visited_coord:
            try:
                risk_dict[(x-1,y)]
            except:
                None
            else:
                largest.append((x-1, y, cost + risk_dict[(x-1,y)]))

        if (x,y+1) not in visited_coord:
            try:
                risk_dict[(x,y+1)]
            except:
                None
            else:
                largest.append((x, y+1, cost + risk_dict[(x,y+1)]))
        
        if (x,y-1) not in visited_coord:
            try:
                risk_dict[(x,y-1)]
            except:
                None
            else:
                largest.append((x, y-1, cost + risk_dict[(x,y-1)]))

    a = min(largest, key=lambda x:x[2])
    visited.append(a)
    visited_at = visited.copy()
    visited_coord.append((a[0],a[1]))
    s += 1
    if s%10 == 0:
        visited_at = remove_coords(visited, visited_at)

    print(visited[-1])



