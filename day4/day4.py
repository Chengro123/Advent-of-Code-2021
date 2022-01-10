import numpy as np 

f = open('input.txt','r')
g = open('numbers.txt','r')

bingo_numbers = [x.split(',') for x in g][0]
bingo_numbers = list(map(int,bingo_numbers))

l = [x.rstrip('\n') for x in f]
boards = [x for x in l if x !='']
boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]

lst = [list(map(int, row.split())) for board in boards for row in board]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

### Now we have all rows and columns in a matrix 

boards_row = list(chunks(lst, 5))
boards_column = [np.array(a).T.tolist() for a in boards_row]

def bingo_game(boards_row,boards_column,bingo_numbers):

    for number in bingo_numbers:

        for rows in boards_row:
            for row in rows:
                if number in row:
                    row.remove(number)
            
        for columns in boards_column:
            for column in columns:
                if number in column:
                    column.remove(number)
        
        rowsum = [[sum(i) for i in row] for row in boards_row]
        columnsum = [[sum(i) for i in column] for column in boards_column]

        for a in rowsum:
            if 0 in a:
                print(sum(a)*number)
                return(a)
        for b in columnsum:
            if 0 in b:
                print(sum(b)*number)
                return(b)
        
bingo_game(boards_row,boards_column,bingo_numbers)


#Part 2

def bingo_game123(boards_row,boards_column,bingo_numbers):

    for number in bingo_numbers:

        for rows in boards_row:
            for row in rows:
                if number in row:
                    row.remove(number)
            
        for columns in boards_column:
            for column in columns:
                if number in column:
                    column.remove(number)
        
        rowsum = [[sum(i) for i in row] for row in boards_row]
        columnsum = [[sum(i) for i in column] for column in boards_column]

        if len(boards_row) != 1 and len(boards_column) != 1:
            count = 0 
            for a,b in list(zip(rowsum,columnsum)):
                if (0 in a) and (0 not in b):
                    boards_row.pop(rowsum.index(a)-count)
                    boards_column.pop(rowsum.index(a)-count)
                    count = count + 1

                elif (0 not in a) and (0 in b):
                    boards_row.pop(columnsum.index(b)-count)
                    boards_column.pop(columnsum.index(b)-count)
                    count = count + 1

                elif (0 in a and b):
                    boards_row.pop(rowsum.index(a)-count)
                    boards_column.pop(columnsum.index(b)-count)
                    count = count + 1

        else: 
            for a in rowsum:
                if 0 in a:
                    print(sum(a)*number)
                    return(a)
            for b in columnsum:
                if 0 in b:
                    print(sum(b)*number)
                    return(b)

bingo_game123(boards_row,boards_column,bingo_numbers)













