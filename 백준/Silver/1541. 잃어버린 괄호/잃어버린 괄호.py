stat = input().split('-') # -로 나눈다

sum_list = []
for i in range(len(stat)):
    sum=0
    #+로 나눈다.
    temp = list(map(int,stat[i].split('+')))
    for j in temp:
        sum+=j
    sum_list.append(sum)

result = sum_list[0]
for i in range(1,len(sum_list)):
    result-=sum_list[i]
print(result)
