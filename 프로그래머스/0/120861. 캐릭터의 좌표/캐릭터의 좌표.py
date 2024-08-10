def solution(keyinput, board):
    result =[0,0]

    max_x = board[0]//2
    min_x = -(board[0]//2)

    max_y = board[1]//2
    min_y = -(board[1]//2)
    
    
    for key in keyinput:
        if key=="left" and result[0] > -(board[0]//2):
            result[0] -= 1
        elif key=="right" and result[0] <(board[0]//2):
            result[0] += 1
        elif key=="up" and result[1] < (board[1]//2):
            result[1]+=1
        elif key=="down" and result[1] > -(board[1]//2):
            result[1]-=1
     
    return result