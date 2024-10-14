from collections import deque
#격자의 크기 n, 초기에 상해 있는 귤의 수k

n, k = map(int,input().split())
step = [[0 for _ in range(n)] for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
visited= [[0 for _ in range(n)] for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

copy_arr = [x[:] for x in arr]

#0귤없음
#1귤있음
#2상한귤있음

#0초에 k개의 상한 귤로 부터 시작하여 1초에 한번 씩 모든 상한 귤로부터 인접한 곳에 있는 귤이 동시에 전부상함

#최초로 상하게 되는 시간

#상해있는 귤의 좌표를 저장한다. 
no_guel = []

def in_range(i,j):
    return 0<=i<n and 0<=j<n

#시간이 step인듯?
def push(i,j,s):
    if step[i][j]>0:
        step[i][j]=min(s,step[i][j])
    else:
        step[i][j]=s
    arr[i][j]=2
    visited[i][j]==1
    q.append((i,j)) 
    #귤 상함 처리
    

#bfs탐색
def bfs():
    s=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==2: #상한 귤을 큐에 집어넣는다.
                push(i,j,s)

    while q:
        si,sj = q.popleft()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = si+di, sj +dj
            
            #격자 안벗어남, 방문안함, 귤이 있는 곳
            if in_range(ni,nj) and visited[ni][nj]==0 and arr[ni][nj]==1:
                push(ni,nj,step[si][sj]+1)

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            step[i][j]=-1 #처음부터 비어 있는 칸
            visited[i][j]=1 #어차피 못감 1로 방문처리 

bfs()


for i in range(n):
    for j in range(n):
        if step[i][j]==0 and arr[i][j]==1:
            step[i][j]=-2

for i in range(n):
    for j in range(n):
        print(step[i][j],end=" ")
    print()           

# 1 1 1
# 1 0 1
# 1 0 2

# #1초뒤
# 1 1 1 0 0 0 
# 1 0 2 0 0 1 
# 1 0 2 0 0 0

# #2초뒤
# 1 1 2 
# 1 0 2
# 1 0 2

# 3초뒤
# 1 2 2
# 1 0 2
# 1 0 2

# 4초뒤
# 2 2 2
# 1 0 2
# 1 0 2

# 5초뒤
# 2 2 2
# 2 0 2
# 1 0 2

# 6초뒤
# 2 2 2
# 2 0 2
# 2 0 2

# 0 0 1 0
# 1 1 1 2
# 0 2 1 0
# 0 0 0 1

# -1 -1 0 -1
# 0 0 0 0
# -1 0 0 -1
# -1 -1 -1 0

# 1 1 0 1
# 0 0 0 0
# 1 0 0 1
# 1 1 1 0

# 1초뒤
# 0 0 1 0 
# 1 2 2 0  
# 0 2 2 0  
# 0 0 0 1  

# -1 -1 0 -1
# 0  1 1   0
# -1 0 1 -1
# -1 -1 -1 0


# 2초뒤
# 0 0 2 0
# 2 2 2 0
# 0 2 2 0
# 0 0 0 1

# -1 -1 2 -1
# 2  1 1   0
# -1 0 1 -1
# -1 -1 -1 0