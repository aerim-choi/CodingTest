def solution(s):
    num_list = s.split(' ')
    stack= []
    sum = 0
    
    
    for ch in num_list:
        if ch =='Z':
            stack.pop()
        else : 
            stack.append(ch)
        
                   
    for i in stack:  
        sum += int(i)
    
    return sum