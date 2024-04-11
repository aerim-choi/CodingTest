def solution(rsp):
    
    win_rsp={
        "2":"0",
        "0":"5",
        "5":"2"
    }
    
    answer = ''
    for i in rsp :
        answer += win_rsp[i]     
    
    return answer