N,M  = map(int, input().split())

rectagle = []
for _ in range(N):
    wb_string = input()
    wb_string = list(wb_string)
    rectagle.append(wb_string)

# 8X8 체스판을 만드는 함수
def make_8x8(row,col,rectagle):
    copy_rectagle = [[0 for _ in range(8)]for _ in range(8)]
    r,c = 0,0
    for i in range(row,row+8):
        c=0
        for j in range(col,col+8):
            copy_rectagle[r][c] =rectagle[i][j]
            c+=1
        r+=1
     
    return copy_rectagle


#지민이가 다시 칠해야하는 정사각형의 최소 개수 계산하는 함수
def calc_change_rectagle(rectagle_8x8):
    # 체스판을 색칠하는 경우는 두가지뿐이다. 하나는 맨 위쪽 위칸이 흰색, 하나는 검정색
    temp = rectagle_8x8[0][0]
    rectagle_8x8[0][0] ='W'
    cnt1,cnt2=0,0
    
    #첫번째 맨위를 흰색이라면
    for row in range(0,8):
        for col in range(0,8):
            if row%2 !=0 and col%2!=0:  #홀수행의 홀수항
               if rectagle_8x8[row][col] != 'W': 
                    cnt1+=1
            elif row%2 !=0 and col%2 ==0 : #홀수행의 짝수항
               if rectagle_8x8[row][col] != 'B':
                   cnt1+=1  
            elif row%2 ==0 and col%2 !=0 : #짝수행의 홀수항
               if rectagle_8x8[row][col] != 'B':
                   cnt1+=1  
            else: #짝수항의 짝수항
                if rectagle_8x8[row][col] != 'W':
                   cnt1+=1  
    if temp != rectagle_8x8[0][0]:
        cnt1+=1
    
    #첫번째 맨위가 검정색이라면
    rectagle_8x8[0][0] ='B'
    for row in range(0,8):
        for col in range(0,8):
            if row%2 !=0 and col%2!=0:  #홀수행의 홀수항
               if rectagle_8x8[row][col] != 'B':
                    cnt2+=1
            elif row%2 !=0 and col%2 ==0 : #홀수행의 짝수항
               if rectagle_8x8[row][col] != 'W':
                   cnt2+=1  
            elif row%2 ==0 and col%2 !=0 : #짝수행의 홀수항
               if rectagle_8x8[row][col] != 'W':
                   cnt2+=1  
            else: #짝수항의 짝수항
                if rectagle_8x8[row][col] != 'B':
                   cnt2+=1  
    if temp != rectagle_8x8[0][0]:
        cnt2+=1
    return min(cnt1,cnt2)


answer= []
#8x8로 탐색
for i in range(0,N-7):
    for j in range(0, M-7):
        copy_rectagle= make_8x8(i,j, rectagle)
        answer.append(calc_change_rectagle(copy_rectagle))

print(min(answer))


'''
WBWBWBwB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBwB
BWBWBWBW
WBWBWBWB
BWBWBWBW 3개
'''


    
    