# 3개의 레벨
# 5 5 5
# 3 4 5
# 2+1+0
# 4개의 레벨
# 5 3 7 5
# 2 3 4 5
# 3+0+3+0

# 각레벨을 클리어할 때 주는 점수가 증가하게 만들어야한다.

N = int(input())
level_scores = []
for i in range(N):
    level_scores.append(int(input()))

cnt= 0
for i in range(N-1,0,-1):
    if level_scores[i-1] >= level_scores[i]:
        while level_scores[i-1] >= level_scores[i]:
            level_scores[i-1] -= 1
            cnt += 1
    else:
        continue

print(cnt)



