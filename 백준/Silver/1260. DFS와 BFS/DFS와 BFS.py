from collections import deque

def main():
    # 정점의 개수 (1<=N<=1000)
    # 간선의 개수 (1<=M<=10000)
    # 탐색을 시작할 정점의 번호 (V)

    N,M,V = map(int, input().split())

    arr = [[0 for j in range(N)]for i in range(N)]

    for i in range(M):
        x,y = map(int, input().split())
        arr[x-1][y-1]=1
        arr[y-1][x-1]=1

    DFS(arr,V-1)
    print()
    BFS(arr,V-1)


def DFS(arr,V):
    stack = [V]
    visited_node = set()

    while stack:
        node = stack.pop()
        if node not in visited_node:
            visited_node.add(node) #방문 노드에 추가
            print(node+1, end=" ")

            for i in range(len(arr[node])-1,-1,-1):
                if arr[node][i] == 1:
                    stack.append(i)

def BFS(arr,V):
    queue = deque([V])
    visited_node = set() # set() , dict

    while queue:
        node = queue.popleft()
        if node not in visited_node:
            visited_node.add(node) #방문 노드에 추가
            print(node + 1, end=" ")

            for i in range(0,len(arr[node]),1):
                if arr[node][i] == 1:
                    queue.append(i)

main()
