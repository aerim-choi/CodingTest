def solution(array, n):
    min_diff= 101
    min_num = 101
    
    array.sort()
    
    for i in array:
        if i <= n : 
            diff = n-i
        else:
            diff = i-n
        
        if min_diff > diff:
            min_diff = diff
            min_num = i
    
    return min_num
