from collections import deque

def bfs(si,sj,color,visited):
    q = deque()
    q.append((si,sj))
    visited[si][sj] == 1

    while q :
        ci,cj = q.popleft()
        #네방향, 범위내, 똑같은 색깔이라면
        for di,dj in((-1,0),(1,0),(0,-1),(0,1)) : #좌우상하
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and RGB_image[ni][nj]==color:
                q.append((ni,nj))
                visited[ni][nj]=1



def solveRGB():  # 적록색맹이 아닌 사람이 봤을 때 구역의 개수
    visited = [[0 for j in range(N)] for i in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(N):
            # 빨간색에 방문했을 경우
            if visited[i][j] == 0 and RGB_image[i][j] == "R":
                bfs(i, j, "R",visited)
                cnt += 1
            # 초록색에 방문했을 경우
            elif visited[i][j] == 0 and RGB_image[i][j] == "G":
                bfs(i,j,"G",visited)
                cnt += 1
            #파란색에 방문했을 경우
            elif visited[i][j]==0 and RGB_image[i][j]=="B":
                bfs(i,j,"B",visited)
                cnt += 1
            else:
                continue

    return cnt

def solveRB():  # 적록생맹이 봤을 때 구역의 개수
    for i in range(N):
        for j in range(N):
            # G를 R로 변경하기
            if RGB_image[i][j] == "G":
                RGB_image[i][j] = "R"

    visited = [[0 for j in range(N)] for i in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(N):
            # 빨간색에 방문했을 경우
            if visited[i][j] == 0 and RGB_image[i][j] == "R":
                bfs(i, j, "R", visited)
                cnt += 1
            # 파란색에 방문했을 경우
            elif visited[i][j]==0 and RGB_image[i][j] == "B":
                bfs(i, j, "B", visited)
                cnt += 1
            else:
                continue

    return cnt


N = int(input())

#RGB 이미지 초기화
RGB_image = [[0 for j in range(N)] for i in range(N)]

#RGM 이미지 값 입력
for i in range(N):
    RGB = input()
    for j in range(N):
        RGB_image[i][j] = RGB[j]


#정답
print(solveRGB(), solveRB())

