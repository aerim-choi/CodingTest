N = int(input()) #사람의 수
P = list(map(int,input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간

P.sort()

result = 0
for i in range(N):
    for j in range(i+1):
        result += P[j]

print(result)


