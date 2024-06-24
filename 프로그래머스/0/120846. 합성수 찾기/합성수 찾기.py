def solution(n):
    answer=[]
    count=0
    for i in range(n,0,-1):
        count=0
        for j in range(1,i+1):
            if i%j == 0 :
                count+=1
                if count>=3:
                    answer.append(i)
                    break
                    
    return len(answer)
            
        
    