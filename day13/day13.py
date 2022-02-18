import matplotlib.pyplot as plt

inputs = open('input.txt','r')
inputs = [list(map(int,(x.strip('\n')).split(','))) for x in inputs]

fold = open('fold.txt','r')
fold = [(x.strip('\n')).split('=') for x in fold]

marks = inputs.copy()

for folding in fold:
    if folding[0] == 'x':
        for coords_x in marks:
            if coords_x[0] > int(folding[1]):
                difference_x = coords_x[0] - int(folding[1])
                coords_x[0] = int(folding[1]) - difference_x
        marks = [list(x) for x in set(tuple(x) for x in marks)]
        print(len(marks))

    elif folding[0] == 'y':
        for coords_y in marks:
            if coords_y[1] > int(folding[1]):
                difference_y = coords_y[1] - int(folding[1])
                coords_y[1] = int(folding[1]) - difference_y
        marks = [list(y) for y in set(tuple(y) for y in marks)]
        print(len(marks))

x_values = [x[0] for x in marks]
y_values = [y[1] for y in marks]

plt.plot(x_values,y_values,'o',color='black')

#ABKJFBGC