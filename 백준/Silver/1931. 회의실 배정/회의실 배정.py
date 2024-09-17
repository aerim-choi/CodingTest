N = int(input()) #회의실 개수
# 회의의 정보
rooms = []
for i in range(N):
    t1,t2 = map(int,input().split())
    rooms.append((t1,t2))

# 끝나는 시간으로 배열을 정렬
rooms.sort(key=lambda x:(x[1],x[0]))

# 첫번째 회의 끝나는 시간<=두번째 회의 시작
reserve_cnt = 1
end_time = rooms[0][1]
for i in range(1,N):
    if rooms[i][0] >= end_time:
        reserve_cnt +=1
        end_time = rooms[i][1]

print(reserve_cnt)