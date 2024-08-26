def solution(board):
    
    for i in range(0,len(board)):
        for j in range(0, len(board[0])):
            if(board[i][j]==1):
                if i-1 >=0 : #위
                    if board[i-1][j]==1:
                        pass
                    else:
                        board[i-1][j]=2
                if i+1<=(len(board)-1): #아래
                    if board[i+1][j]==1:
                        pass
                    else:
                        board[i+1][j]=2
                
                if j-1>=0 :#왼
                    if board[i][j-1]==1:
                        pass
                    else:
                        board[i][j-1]=2
                        
                if j+1<=(len(board[0])-1):#오
                    if board[i][j+1]==1:
                        pass
                    else:
                        board[i][j+1]=2
                    
                if i-1>=0 and j-1>=0:#왼위
                    if board[i-1][j-1]==1:
                        pass
                    else:
                        board[i-1][j-1]=2
                if i-1>=0 and j+1<=(len(board[0])-1):#왼아래
                    if board[i-1][j+1]==1:
                        pass
                    else:
                        board[i-1][j+1]=2
                    
                if i+1<=(len(board)-1) and j-1>=0:#오윈
                    if board[i+1][j-1]==1:
                        pass
                    else:
                        board[i+1][j-1]=2
                if i+1<=(len(board)-1) and j+1<=(len(board[0])-1):#오아래
                    if board[i+1][j+1]==1:
                        pass
                    else:
                        board[i+1][j+1]=2
                
    result=0              
    for i in range(0,len(board)):
        for j in range(0, len(board[0])):    
            print(board[i][j],end="")
            if board[i][j]==2 or board[i][j]==1:
                result+=1
        print()
        
    return len(board)*len(board[0])-result
