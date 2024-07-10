def solution(rows, columns, queries):
    answer = []
    table = [[0 for j in range(columns)] for i in range(rows)]
    num=1
    #행렬만들기
    for i in range(0, rows):
        for j in range(0, columns):
            table[i][j]=num
            num+=1
    
    #최솟값 구하기
    for query in queries:
        print(query)
        row1= query[0]-1 #1 
        col1= query[1]-1 #1 
        row2= query[2]-1 #4
        col2= query[3]-1 #3
        border_list = [] #테두리 숫자를 담을 리스트
        #최솟값 구하기
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                if i == row1 or i ==row2 :
                    border_list.append(table[i][j])
                else: 
                    continue
            if not (i == row1 or i ==row2) :
                border_list.append(table[i][col1])
                border_list.append(table[i][col2])

        answer.append(min(border_list))
        
        temp_table =  [[0 for j in range(columns)] for i in range(rows)]
        
        #2차원 배열 복사
        for i in range(rows):
            for j in range(columns):
                temp_table[i][j]=table[i][j] 
        #회전하기
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                if i==row1 and j ==col1: #테두리 첫번째행의 첫번째열
                    table[i][j]= temp_table[i+1][j]
                elif i == row1 :#맨위 테두리
                    table[i][j] = temp_table[i][j-1]
                elif i==row2 and j==col2: #맨아래 테두리 마지막행 마지막열
                    table[i][j]=temp_table[i-1][j]
                elif i ==row2:#맨아래 테두리
                    table[i][j]=temp_table[i][j+1]
                elif j==col1 :
                    table[i][j]=temp_table[i+1][j]
                elif j==col2:
                    table[i][j]=temp_table[i-1][j]
                else:
                    continue
    return answer  
    

# # [2,2,5,4] -> 행렬 인덱스 [1,1,4,3]
# 2 34 5         1 2 3 4
# # 234            123  
# table[1][1] table[1][2] table[1][3]
# table[2][1]             table[2][3]
# table[3][1]             table[3][3]
# table[4][1] table[4][2] table[4][3]

# table[2][1] table[1][1] table[1][2]
# table[3][1]             table[1][3]
# table[4][1]             table[2][3]
# table[4][2] table[4][3] table[3][3]


# [3,3,6,6] ->행렬인덱스 [2,2,5,5]
# 3 45 6       2 34 5
# 3 45 6       2345

# 행렬 인덱스 [2,2,5,5]
# table[2][2] table[2][3] table[2][4] table[2][5]
# table[3][2]                         table[3][5]
# table[4][2]                         table[4][5]
# table[5][2] table[5][3] table[5][4] table[5][5]

# table[3][2] table[2][2] table[2][3] table[2][4]
# table[4][2]                         table[2][5]
# table[5][2]                         table[3][5]
# table[5][3] table[5][4] table[5][5] table[4][5]

