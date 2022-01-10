f = open('input.txt','r')
l = [x.rstrip("\n") for x in f]
forwards = [int(x.replace("forward ",'')) for x in l if 'forward' in x]
ups = [int(x.replace("up ",'')) for x in l if 'up' in x]
downs = [int(x.replace("down ",'')) for x in l if 'down' in x]

print(sum(forwards)*(sum(downs) - sum(ups)))

#Part 2

aim = 0 
depth = 0
for x in l:
    if 'down' in x:
        aim = aim + int(x.replace("down ",''))
    elif 'up' in x:
        aim = aim - int(x.replace("up ",''))
    elif 'forward' in x:
        depth = depth + aim*int(x.replace("forward ",''))
        
print(depth*sum(forwards))

