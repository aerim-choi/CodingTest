def dfs(n,sm):
    global ans

    if n>=N:
        ans = max(ans,sm)
        return
    if n+T[n]<=N: #상담을 하는 경우(퇴사일전 완료가능할 경우)
        dfs(n+T[n],sm+P[n])
    dfs(n+1,sm) #상담을 하지 않는 경우(항상 가능, 다음날로 상담)

N= int(input())
T = [0]*N
P = [0]*N

for i in range(N):
    T[i],P[i] = map(int,input().split())

ans = 0
dfs(0,0)
print(ans)