from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    
    area = 1
    
    while q:
        ci,cj = q.popleft()
        
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = ci+di, cj+dj 
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and visited[ni][nj]==0:
                 q.append((ni,nj))
                 visited[ni][nj] = 1
                 area+=1 
                
    return area


def solve():
    max_area=0
    cnt_area = 0 #그림의 개수
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and visited[i][j]==0: #그림이 그려져있고, 방문하지 않았다면
                max_area=max(max_area,bfs(i,j)) 
                cnt_area+=1 

    print(cnt_area)
    print(max_area)
    



# 입력
n,m= map(int,(input().split()))
arr=[[0 for j in range(m)] for i in range(n)]
visited = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    draw = input()
    draw_array = draw.split()
    for j in range(m):
        arr[i][j]= int(draw_array[j])

solve()