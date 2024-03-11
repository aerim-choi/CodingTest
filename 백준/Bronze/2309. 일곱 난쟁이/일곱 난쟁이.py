import itertools 
list = [int(input()) for _ in range(9)]

for com in itertools.combinations(list,7):
    if sum(com) == 100 : 
        for j in sorted(com):
            print(j)
        break