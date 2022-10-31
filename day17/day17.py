# input x=138..184, y=-125..-71

# Part 1, using math 7750

# Part 2 

xlow, xhigh = 138, 184
ylow, yhigh = -125, -71

# x velocities can be between 17 and xhigh
# y velocities can be between ylow and -ylow-1 

def simulation(xvel, yvel, x = 0, y = 0):
    if xlow <= x <= xhigh and ylow <= y <= yhigh:
        return 1
    elif y < ylow or x > xhigh:
        return 0
    elif xvel == 0 and not (xlow <= x <= xhigh):
        return 0 
    elif xvel == 0: 
        return simulation(xvel, yvel - 1, x + xvel, y + yvel)
    else:
        return simulation(xvel - 1, yvel - 1, x + xvel, y + yvel)
    
count = sum([simulation(x,y) for x in range(17, xhigh + 1) for y in range(ylow, -ylow)])




