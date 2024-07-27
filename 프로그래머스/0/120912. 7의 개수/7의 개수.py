def solution(array):
    answer = 0
    for num in array: 
        num = str(num)
        if '7' in num:
            answer+= num.count('7')
        
        
    return answer