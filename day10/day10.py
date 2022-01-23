from collections import Counter
import statistics

f = open('input.txt','r')
inputs = [x.strip('\n') for x in f]
new_inputs = [[chunk for chunk in chunks] for chunks in inputs]

for chunks in new_inputs:

    for n,chunk in enumerate(chunks):

        if chunk == '(':
            chunks[n] = 3
        elif chunk == ')':
            chunks[n] = -3

        elif chunk == '[':
            chunks[n] = 57
        elif chunk == ']':
            chunks[n] = -57

        elif chunk == '{':
            chunks[n] = 1197
        elif chunk == '}':
            chunks[n] = -1197

        elif chunk == '<':
            chunks[n] = 25137
        elif chunk == '>':
            chunks[n] = -25137

def somefunction(numbered_chunks,test):
    for numbered_chunk in numbered_chunks:
        if numbered_chunk < 0:
            i = test.index(numbered_chunk)
            if abs(test[i]) == test[i-1]:
                del test[i-1:i+1]
            else:
                return(numbered_chunk)

answer_list = []
for numbered_chunks in new_inputs:
    test = numbered_chunks[:]
    answer_list.append(somefunction(numbered_chunks,test))

answer = 0
for key, value in Counter(answer_list).items():
    if key == None:
        None
    else: 
        answer = answer + abs(key)*value

print(answer)

# Part 2 

def somefunction_2(numbered_chunks,test):
    for numbered_chunk in numbered_chunks:
        if numbered_chunk < 0:
            i = test.index(numbered_chunk)
            if abs(test[i]) == test[i-1]:
                del test[i-1:i+1]
            else:
                return([])
    return(test)

answer_list_2 = []
for numbered_chunks in new_inputs:
    test = numbered_chunks[:]
    answer_list_2.append(somefunction_2(numbered_chunks,test))

answer_list_2 = [x[::-1] for x in answer_list_2 if x != []]

def strange_calculator(completion_list):
    score = 0
    for syntax in completion_list:
        if syntax == 3:
            score = score*5 + 1
        elif syntax == 57:
            score = score*5 + 2
        elif syntax == 1197:
            score = score*5 + 3
        elif syntax == 25137:
            score = score*5 + 4
    return(score)

final_answer = [strange_calculator(syntaxes) for syntaxes in answer_list_2]
print(statistics.median(final_answer))

            






